import pytest


def test_hook(cmdopt):
    print(f"{cmdopt}")


if __name__ == "__main__":
    pytest.main(["-s", "--env=dev", "test_hook.py"])
