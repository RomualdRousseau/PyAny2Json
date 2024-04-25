import os
import jpype
import requests

LIB_PATH = "libs"
JAR_PATH = "jars"
MAVEN_URL = "https://oss.sonatype.org/content/repositories/releases"
MAVEN_SNAPSHOT_URL = "https://oss.sonatype.org/content/repositories/snapshots"
DEPENDENCIES = [
    "com.github.romualdrousseau:shuju:jar:1.23"
]

jpype.startJVM(classpath=[f"{JAR_PATH}/*", f"{LIB_PATH}/*"])


def install_one_dependency(dep):
    parts = dep.split(':')
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
    
    if os.path.exists(f"{JAR_PATH}/{file_name_disk}"):
        return    
    
    url = '/'.join([base_url, package.replace('.', '/'), name, version, file_name])
    print(url)
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{JAR_PATH}/{file_name_disk}", "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    if not os.path.exists(JAR_PATH):
        os.mkdir(JAR_PATH)
        
    with open("dependencies", "r") as file:
        dependencies = file.readlines()
        
    for dep in dependencies:
        install_one_dependency(dep.rstrip())
