import requests

BASE_URL = "http://127.0.0.1:5000"

def add_user():
    res = requests.post(f"{BASE_URL}/add", json={"user": "test"})
    print(res.json())

def check_status():
    res = requests.get(f"{BASE_URL}/status/test")
    print(res.json())

def remove_user():
    res = requests.post(f"{BASE_URL}/remove", json={"user": "test"})
    print(res.json())

if __name__ == "__main__":
    add_user()
    check_status()
    remove_user()
    check_status()