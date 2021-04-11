import base64
import requests
import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config-secret.ini")

    BASE_URL = config["main"]["BASE_URL"]
    userAndPass = base64.b64encode(bytes(f"{config['auth']['client_id']}:{config['auth']['client_id']}"
                                         .encode("utf-8"))).decode("ascii")

    print(userAndPass)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {userAndPass}",
    }
    url = f"{BASE_URL}connect/oauth2/token"
    print(url)
    r = requests.get(url, headers=headers)
    print(r.status_code)
