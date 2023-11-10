import json
import time
import requests


def test_1_create_user():
    create_user_url = "https://petstore.swagger.io/v2/user"

    user_data = {
        "id": 123,
        "username": "testuser",
        "firstName": "John",
        "lastName": "Doe",
        "email": "testuser@example.com",
        "password": "securepassword",
        "phone": "1234567890",
    }

    response = requests.post(create_user_url, json=user_data)

    assert response.status_code == 200

    response_json = response.json()
    assert response_json["code"] == 200

    assert response_json["message"] == "123", f"Unexpected user ID in the response: {response_json['message']}"


def test_2_login_user():
    login_url = "https://petstore.swagger.io/v2/user/login"

    login_data = {
        "username": "testuser",
        "password": "securepassword",
    }
    response = requests.get(login_url, params=login_data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["code"] == 200


def test_3_user_list():
    user_list_url = "https://petstore.swagger.io/v2/user/createWithList"

    list_of_users = [
        {
            "id": 1,
            "username": "user1",
            "firstName": "John",
            "lastName": "Doe",
            "email": "user1@example.com",
            "password": "securepassword1",
            "phone": "1234567890",
            "userStatus": 0
        },
        {
            "id": 2,
            "username": "user2",
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "user2@example.com",
            "password": "securepassword2",
            "phone": "9876543210",
            "userStatus": 0
        }
    ]
    response = requests.post(user_list_url, json=list_of_users)
    assert response.status_code == 200


def test_4_logout_user():
    logout_url = "https://petstore.swagger.io/v2/user/logout"

    response = requests.get(logout_url)
    assert response.status_code == 200


def test_5_add_pet():
    add_pet_url = "https://petstore.swagger.io/v2/pet"

    new_pet = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Flex",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    new_pet_json = json.dumps(new_pet)
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(add_pet_url, data=new_pet_json, headers=headers)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["name"] == "Flex"

def test_6_update_pet():

    add_pet_url = "https://petstore.swagger.io/v2/pet"

    new_pet = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Flex",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.post(add_pet_url, json=new_pet)

    if response.status_code == 200:
        pet_data = response.json()
        new_pet_id = pet_data["id"]
        print("New pet added with ID:", new_pet_id)

        time.sleep(2)

    updated_pet_data = {
        "id":new_pet_id,
        "name": "NewName",  # New name for the pet
        "status": "sold"  # New status for the pet
    }

    # URL to update a pet's data
    update_pet_url ="https://petstore.swagger.io/v2/pet/{new_pet_id}"

    response = requests.post(update_pet_url, json=updated_pet_data)

    if response.status_code == 200:
        print("Pet with ID {'new_pet_id'} updated successfully.")



def test_7_delete_pet():

    add_pet_url = "https://petstore.swagger.io/v2/pet"


    new_pet = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Flex",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }


    response = requests.post(add_pet_url, json=new_pet)

    if response.status_code == 200:
        pet_data = response.json()
        new_pet_id = pet_data["id"]
        print("New pet added with ID:", new_pet_id)

        time.sleep(2)

        delete_pet_url = f"https://petstore.swagger.io/v2/pet/{new_pet_id}"
        delete_response = requests.delete(delete_pet_url)
        if delete_response.status_code == 200:
            print("Pet with ID", new_pet_id, "deleted successfully.")
        else:
            print("Failed to delete pet. Status code:", delete_response.status_code)
    else:
        print("Failed to add a new pet. Status code:", response.status_code)

