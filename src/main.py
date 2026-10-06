"""Este módulo é um teste para o GitHub Actions."""

import requests

print("Hello World!")

def request():
    """Função request"""
    response = requests.get("https://google.com", timeout=5)
    print(response.status_code)
    return response.status_code

if __name__ == "__main__":
    request()
