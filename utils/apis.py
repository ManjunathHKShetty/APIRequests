from utils.helpers import (api_get, api_post, api_put, api_delete, api_file_upload, api_file_download)

class APIs:
    def __init__(self, auth_token):
        self.auth_token = auth_token

    def get(self, endpoint):
        return api_get(self.auth_token, endpoint)

    def post(self, endpoint, user_data):
        return api_post(self.auth_token, endpoint, user_data)

    def put(self, endpoint, user_data):
        return api_put(self.auth_token, endpoint, user_data)

    def delete(self, endpoint):
        return api_delete(self.auth_token, endpoint)

    def file_upload(self):
        return api_file_upload()

    def file_download(self):
        return api_file_download()
