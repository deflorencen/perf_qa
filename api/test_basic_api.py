import requests, pytest

@pytest.fixture
def obj_id():
    payload = {
        "name": "Google Pixel 6 Pro",
        "data": {
            "color": "Cloudy White",
            "capacity": "128 GB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=payload).json()
    yield response["id"]
    requests.delete(f"https://api.restful-api.dev/objects/{response['id']}")

def test_get_data_from_json():
    payload = {
        "name": "Google Pixel 6 Pro",
        "data": {
            "color": "Cloudy White",
            "capacity": "128 GB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=payload).json()

    assert response["name"] == payload["name"]
    assert response["data"]["color"] == payload["data"]["color"]
    assert response["data"]["capacity"] == payload["data"]["capacity"]


def test_get_data_from_id(obj_id):
    response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}").json()
    print(response)

    assert response["id"] == obj_id


def test_update_data(obj_id):
    payload = {
        "name": "Google Pixel 6 Pro",
        "data": {
            "color": "Cloudy White",
            "capacity": "128 GB",
            "year": "2021",
            "RAM": "12 GB"
        }
    }
    response = requests.put(f"https://api.restful-api.dev/objects/{obj_id}", json=payload).json()
    print(response)

    assert response["data"]["year"] == payload["data"]["year"]
    assert response["data"]["RAM"] == payload["data"]["RAM"]


def test_delete_data(obj_id):
    response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
    assert response.status_code == 200
    response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}")
    assert response.status_code == 404
