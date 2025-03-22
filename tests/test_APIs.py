import json
import pytest
import allure
from utils.apis import APIs
from utils.logger import LogGen
from utils.libs import Libs

logger = LogGen.loggen()

@pytest.fixture(scope="module")
def apis(auth_token):
    return APIs(auth_token)

@pytest.fixture(scope="module")
def user_id(apis):
    return Libs.post_user(apis)[0]

@allure.severity(allure.severity_level.NORMAL)
def test_get_users(apis):
    logger.info("GETTING USERS......")
    json_str = Libs.get_users(apis)
    logger.info(f"json GET response body: {json_str}")
    logger.info("GET USER IS DONE.....")

@allure.severity(allure.severity_level.NORMAL)
def test_post_user(apis):
    logger.info("ADDING THE USER......")
    user_id, json_str = Libs.post_user(apis)
    logger.info(f"user id ===>> {user_id}")
    logger.info(f"json POST response body: {json_str}")
    logger.info("POST USER IS DONE.....")

@allure.severity(allure.severity_level.NORMAL)
def test_put_user(apis, user_id):
    logger.info("UPDATING THE USER......")
    json_str = Libs.put_user(apis, user_id)
    logger.info(f"json PUT response body: {json_str}")
    logger.info("UPDATE USER IS DONE.....")

@allure.severity(allure.severity_level.NORMAL)
def test_delete_user(apis, user_id):
    logger.info("DELETING THE USER.....")
    Libs.delete_user(apis, user_id)
    logger.info("DELETE USER IS DONE.....")
    logger.info("END OF API TESTING")

@allure.severity(allure.severity_level.NORMAL)
def test_upload_file(apis):
    logger.info("UPLOADING THE FILE.......")
    Libs.upload_file(apis)
    logger.info("SUCCESSFULLY UPLOADED FILE")

@allure.severity(allure.severity_level.NORMAL)
def test_download_file(apis):
    logger.info("DOWNLOADING THE FILE.......")
    Libs.download_file(apis)
    logger.info("SUCCESSFULLY DOWNLOADED FILE")
