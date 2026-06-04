import importlib.util
import pytest


@pytest.fixture
def terminal02():
    """Carrega src/02_terminal.py como módulo, sem executá-lo."""
    spec = importlib.util.spec_from_file_location("terminal02", "src/02_terminal.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
