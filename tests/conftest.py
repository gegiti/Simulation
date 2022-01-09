import pytest


@pytest.fixture
def fix():
    # Setup
    yield None
    # Cleanup
