import logging
import os
import shutil
from importlib import resources

import jpype
import jpype.imports
import requests
from tqdm import tqdm

from .config import MAVEN_SNAPSHOT_URL, MAVEN_URL
from .version import __version__

# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__package__)


def install_one_dependency(jars_path, dep, pbar=None):
    parts = dep.split(":")
    if len(parts) == 4:
        package, name, extension, version = parts
        file_name = f"{name}-{version}.{extension}"
        file_name_disk = file_name
        base_url = MAVEN_URL
    else:
        package, name, extension, oz, version = parts
        if "SNAPSHOT" in version:
            v = version.replace("-SNAPSHOT", "")
            file_name = f"{name}-{v}-{oz}.{extension}"
            file_name_disk = f"{name}-{version}.{extension}"
            base_url = MAVEN_SNAPSHOT_URL
        else:
            file_name = f"{name}-{version}-{oz}.{extension}"
            file_name_disk = file_name
            base_url = MAVEN_URL

    if os.path.exists(f"{jars_path}/{file_name_disk}"):
        return

    url = "/".join([base_url, package.replace(".", "/"), name, version, file_name])

    if pbar:
        pbar.set_description(f"Downloading {file_name}")

    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{jars_path}/{file_name_disk}", "wb") as file:
            file.write(response.content)


def install_all_dependencies(jars_path, deps_path):
    os.mkdir(jars_path)
    with open(deps_path, "r") as file:
        dependencies = file.readlines()
        pbar = tqdm(dependencies, desc="Loading dependencies")
        for dep in pbar:
            install_one_dependency(jars_path, dep.rstrip(), pbar)


def start_java_archery_framework():
    if jpype.isJVMStarted():
        return

    package_path = resources.files(__package__)
    jars_path = package_path.parent / f"{__package__}.jars"
    libs_path = package_path.parent / f"{__package__}.libs"
    deps_path = package_path / "dependencies"

    options = [
        "-ea",
        "--add-opens=java.base/java.nio=ALL-UNNAMED",
        "--enable-native-access=ALL-UNNAMED",
        # "--sun-misc-unsafe-memory-access=allow",
    ]

    classpath = [f"{jars_path}/*", f"{libs_path}/*"]

    logger.info("Start JVM with the following parameters:")
    logger.info(f"Options: {options}")
    logger.info(f"Classpath: {classpath}")

    expected_jar = jars_path / f"archery-{__version__}.jar"
    if os.path.exists(jars_path) and not os.path.exists(expected_jar):
        logger.info(f"Version mismatch or missing jar. Expected archery-{__version__}.jar. Reinstalling dependencies.")
        shutil.rmtree(jars_path)

    if not os.path.exists(jars_path):
        install_all_dependencies(jars_path, deps_path)

    jpype.startJVM(*options, classpath=classpath)


start_java_archery_framework()
logger.warning(f"JAVA ARCHERY FRAMEWORK {__version__} LOADED")
