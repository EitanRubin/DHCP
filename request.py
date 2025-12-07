import requests

import requests

class GetIP:
    
    @staticmethod

    def get_ip(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            raise Exception(f"Request failed with status {response.status_code}")


#print(GetIP.get_ip("https://noncultured-unenviously-iesha.ngrok-free.dev/get-ip"))
