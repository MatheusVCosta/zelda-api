# class for connect with zelda api


import requests

from app.config.config import get_settings

class ZeldaAPIConnector: 
    def base_ulr():
        return get_settings().zelda_api
    
    @classmethod
    def fetch_all_games(self):
        full_url = "{0}/games?limit=1".format(self.base_ulr())
        return self.execute_request(full_url)
    
    @classmethod
    def execute_request(self, url):
        headers = {"content-type": "application/json"}
        response = requests.get(url, headers=headers, timeout=5, verify=True)

        if response.status_code > 299:
            warning_message = f"Certifix.request.get returning some error. Request_URL{ url } | Response_status={ response.status_code }"
            print(warning_message)
            if response.status_code == 404:
                print(
                    f"Not found Reques_URL={url} | Response_status={response.status_code}"
                )
                return None

        return response.json()
    