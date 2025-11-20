import jpype
import pytest

from pyarchery.setup import start_java_archery_framework


def test_jvm_initialization():
    """Test that the JVM starts correctly and is idempotent."""
    # Ensure JVM is started (it might be started by other tests or __init__)
    start_java_archery_framework()
    assert jpype.isJVMStarted()


def test_jvm_idempotency():
    """Test that calling start_java_archery_framework multiple times doesn't crash."""
    # This should be safe to call even if already started
    try:
        start_java_archery_framework()
        start_java_archery_framework()
    except Exception as e:
        pytest.fail(f"start_java_archery_framework raised exception on repeated call: {e}")

    assert jpype.isJVMStarted()
