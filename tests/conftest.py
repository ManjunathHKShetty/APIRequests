import pytest
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{reports_dir}/report_{now}.html"

@pytest.fixture(scope='session',autouse=True)
def auth_token():
    return "Bearer 62b7d2d686e7bc8f69f7ff576e688a843e50361834c1c43655b4ad9c837166d4"
