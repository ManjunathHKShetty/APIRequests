import json
import pytest
import allure
from utils.apis import APIs
from utils.logger import LogGen
from utils.helpers import generate_random_email
from utils.libs import assert_status_code, assert_response_contains_field, assert_field_value

logger = LogGen.loggen()

@pytest.fixture(scope="module")
def apis(auth_token):
    return APIs(auth_token)

@allure.severity(allure.severity_level.NORMAL)
def test_get_users(apis):
    logger.info("GETTING USERS......")
    response = apis.get("/public/v2/users")
    assert_status_code(response, 200)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    logger.info(f"json GET response body: {json_str}")
    logger.info("GET USER IS DONE.....")

@allure.severity(allure.severity_level.NORMAL)
def test_post_user(apis):
    logger.info("ADDING THE USER......")
    user_data = {
        "name": "John Automation",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = apis.post("/public/v2/users/", user_data)
    assert_status_code(response, 201)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    logger.info(f"json GET response body: {json_str}")
    user_id = json_data["id"]
    logger.info(f"user id ===>> {user_id}")
    assert_response_contains_field(json_data, 'name')
    assert_field_value(json_data, 'name', "John Automation")
    logger.info("POST USER IS DONE.....")

@pytest.fixture(scope="module")
def user_id(apis):
    user_data = {
        "name": "John Automation",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = apis.post("/public/v2/users/", user_data)
    json_data = response.json()
    return json_data["id"]

@allure.severity(allure.severity_level.NORMAL)
def test_put_user(apis, user_id):
    logger.info("UPDATING THE USER......")
    user_data = {
        "name": "John Automation Labs",
        "email": generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = apis.put(f"/public/v2/users/{user_id}", user_data)
    assert_status_code(response, 200)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    logger.info(f"json GET response body: {json_str}")
    assert_field_value(json_data, "id", user_id)
    assert_field_value(json_data, "name", "John Automation Labs")
    assert_field_value(json_data, "gender", "male")
    logger.info("UPDATE USER IS DONE.....")

@allure.severity(allure.severity_level.NORMAL)
def test_delete_user(apis, user_id):
    logger.info("DELETING THE USER.....")
    response = apis.delete(f"/public/v2/users/{user_id}")
    assert_status_code(response, 204)
    logger.info("DELETE USER IS DONE.....")
    logger.info("END OF API TESTING")
