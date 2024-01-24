# class for connect with zelda api


import requests

from app.config.config import get_settings

class ZeldaAPIConnector: 
    def base_ulr():
        return get_settings().zelda_api
    
    @classmethod
    def fetch_all_games(
        self,
        params : list = None
    ):
        limit = 1
        if params:
            limit = params['limit']
            
        full_url = "{0}/games?limit={1}".format(self.base_ulr(), limit)
        return self.execute_request(full_url)
    
    @classmethod
    def execute_request(self, url):
        headers = {"content-type": "application/json"}
        response = requests.get(url, headers=headers, timeout=5, verify=True)

        if response.status_code > 299:
            response_message = {
                "message" : f"request.get returning some error. Request_URL{ url }",
                "status" : response.status_code
            }
            if response.status_code == 404:
                response_message = {
                    "message" : f"Not found Reques_URL={url}",
                    "status" : response.status_code
                }
                
            print(response_message["message"])
            return response_message
        
        return response.json()
    