import pytest
import configparser
from datetime import datetime
from apis import APIs
from tests.helpers import Helpers
from utils.logger import LogGen

logger = LogGen.loggen()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{reports_dir}/report_{now}.html"


config = configparser.ConfigParser()
config.read("config.ini")


@pytest.fixture(scope='session', autouse=True)
def auth_token():
    return config.get("Auth", "bearer_token")


@pytest.fixture(scope="module")
def apis(auth_token):
    logger.info("Creating APIs instance")
    return APIs(auth_token)


@pytest.fixture(scope="module")
def user_id(apis):
    logger.info("Fixture Auth Token & User ID")
    response = Helpers.post_user(apis)
    user_id = response[0]
    return user_id
