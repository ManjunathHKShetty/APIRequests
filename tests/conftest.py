import pytest
import configparser
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{reports_dir}/report_{now}.html"

config = configparser.ConfigParser()
config.read("config.ini")

@pytest.fixture(scope='session',autouse=True)
def auth_token():
    return config.get("Auth", "bearer_token", fallback=os.getenv("AUTH_TOKEN", "default_token"))
