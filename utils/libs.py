import json
import os

from utils.string_helpers import generate_random_email


class Libs:
    @staticmethod
    def get_users(apis):
        response = apis.get("/public/v2/users")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        json_data = response.json()
        return json.dumps(json_data, indent=4)

    @staticmethod
    def post_user(apis):
        user_data = Libs._generate_user_data()
        response = apis.post("/public/v2/users/", user_data)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        json_data = response.json()
        assert "id" in json_data, "User ID not found in response"
        assert json_data["name"] == "John Automation", (
            f"Expected name to be 'John Automation', but got '{json_data['name']}'"
        )
        user_id = json_data["id"]
        return user_id, json.dumps(json_data, indent=4)

    @staticmethod
    def put_user(apis, user_id):
        user_data = Libs._generate_user_data(name="John Automation Labs", status="inactive")
        response = apis.put(f"/public/v2/users/{user_id}", user_data)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        json_data = response.json()
        assert json_data["id"] == user_id, f"Expected ID to be '{user_id}', but got '{json_data['id']}'"
        assert json_data["name"] == "John Automation Labs", (
            f"Expected name to be 'John Automation Labs', but got '{json_data['name']}'"
        )
        assert json_data["gender"] == "male", "Gender mismatch in response"
        return json.dumps(json_data, indent=4)

    @staticmethod
    def delete_user(apis, user_id):
        response = apis.delete(f"/public/v2/users/{user_id}")
        assert response.status_code == 204, f"Expected 204, got {response.status_code}"

    @staticmethod
    def _generate_user_data(name="John Automation", email=None, gender="male", status="active"):
        return {
            "name": name,
            "email": email if email else generate_random_email(),
            "gender": gender,
            "status": status
        }

    @staticmethod
    def upload_file(apis):
        response = apis.file_upload()
        assert response and response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    @staticmethod
    def download_file(apis):
        file_path, response = apis.file_download()
        assert response.status_code == 200
        assert os.path.exists(file_path), "Downloaded file does not exist!"