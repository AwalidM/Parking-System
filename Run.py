import requests

files_to_check = [
    "index.html",
    "home.html",
    "login.html",
    "signup.html",
    "dashbord.html",
    "slots.html",
    "auth.js",
    "scripts.js"
]

BASE_URL = "https://github.com/AwalidM/Parking-System"

for file in files_to_check:
    url = f"{BASE_URL}/{file}"
    try:
        response = requests.get(url)
        print(f"Checked {url}: HTTP {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed to reach {url}: {e}")
