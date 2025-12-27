import requests

def get_ip():
    """Fetch your public IP address."""
    response = requests.get("https://api.ipify.org?format=json", timeout=5)
    return response.json()["ip"]

if __name__ == "__main__":
    print(f"My public IP is: {get_ip()}")