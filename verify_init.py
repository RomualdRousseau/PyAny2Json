import os
import sys

# Add src to python path
sys.path.insert(0, os.path.abspath("src"))

import jpype
import pyarchery

print("First initialization...")
# This happens on import of pyarchery
if jpype.isJVMStarted():
    print("JVM started successfully.")
else:
    print("JVM NOT started.")
    sys.exit(1)

print("Second initialization (idempotency check)...")
from pyarchery.setup import start_java_archery_framework

try:
    start_java_archery_framework()
    print("Idempotency check passed (no crash).")
except Exception as e:
    print(f"Idempotency check FAILED: {e}")
    sys.exit(1)
