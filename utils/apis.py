import requests
class APIs:
    BASE_URL = "https://gorest.co.in/"

    def __init__(self, auth_token):
        self.headers = {"Authorization": auth_token, "Content-Type": "application/json"}

    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url=url, headers=self.headers)
        return response


    def post(self, endpoint, user_data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, json=user_data, headers=self.headers)
        return response

    def put(self, endpoint, user_data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, json=user_data, headers=self.headers)
        return response

    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url, headers=self.headers)
        return response

