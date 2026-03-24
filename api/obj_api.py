from playwright.sync_api import APIRequestContext

class ObjectsApi:
    def __init__(self, request: APIRequestContext):
        self.request = request
        self.endpoint = "/objects"

    def create_object(self, payload: dict):
        return self.request.post(self.endpoint, data=payload)

    def delete_object(self, obj_id: str):
        return self.request.delete(f"{self.endpoint}/{obj_id}")

    def get_object(self, obj_id: str):
        return self.request.get(f"{self.endpoint}/{obj_id}")