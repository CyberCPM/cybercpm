import requests
import os
import json
from time import sleep

# © Lynx | DPR_LynX_Lovers — 2025
# No stealing. No tracing. No funny business.
# Engineered in the shadows by DPRLynX on June 16th, 2025

BASE_URL: str = "https://admincpm.io/chanxreyno2/api"

class Emritz:
    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
        self.datapath = "dataplayer/cars"
    
    def login(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/account_login", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")

    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded
    
    def get_key_data(self) -> any:
        params = { "key": self.access_key }
        response = requests.get(f"{BASE_URL}/get_key_data", params=params)
        response_decoded = response.json()
        return response_decoded
 
    def save_player_car(self, car_data: dict) -> bool:
        url = f"{BASE_URL}/set_car"
        params = {"key": self.access_key}
        payload = {
            "account_auth": self.auth_token,
            "content": car_data
        }
        response = requests.post(url, params=params, json=payload)
        try:
            response_decoded = response.json()
            return response_decoded.get("ok", False)
        except Exception:
            return False
          
    def save_player_money(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/save_money", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def save_player_name(self, name) -> bool:
        payload = { "account_auth": self.auth_token, "name": name }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/save_name", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def levels_done(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/levels_done", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def face_male(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/face_male", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def face_female(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/face_female", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def attribute_male(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/attribute_male", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def attribute_female(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/attribute_female", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def all_animations_unlocked(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/all_animations_unlocked", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def all_home_unlocked(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/all_home_unlocked", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def all_paint_unlocked(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/all_paint_unlocked", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def all_wheels_unlocked(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/all_wheels_unlocked", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def all_calipers_unlocked(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/all_calipers_unlocked", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlocked_police(self, car_data) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "car_data": json.dumps(car_data)
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlocked_police", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def all_sound_police_unlocked(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/all_sound_police_unlocked", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlocked_bodykits(self, car_data) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "car_data": json.dumps(car_data)
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlocked_bodykits", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def swap_gearbox_awd(self, car_data) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "car_data": json.dumps(car_data)
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/swap_gearbox_awd", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def get_all_player_cars(self) -> any:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/get_all_cars", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            datacar = response_decoded.get("datacar", {})
            folder = "dataplayer/cars"
            if not os.path.exists(folder):
                os.makedirs(folder)
            else:
                for f in os.listdir(folder):
                    os.remove(os.path.join(folder, f))
            for car_id, car_data in datacar.items():
                filename = os.path.join(folder, car_id)
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(car_data, f, indent=4, ensure_ascii=False)
            return datacar
        return None

    def save_player_slots_collection(self) -> bool:
        car_instance_ids = []
        folder_path = "dataplayer/cars"
    
        for filename in os.listdir(folder_path):
            name, ext = os.path.splitext(filename)
            if name.isdigit():
                file_path = os.path.join(folder_path, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = json.load(file)
                        car_instance_id = content.get("data", {}).get("CarInstanceId")
                        if car_instance_id:
                            car_instance_ids.append(car_instance_id)
                except:
                    continue
    
        if not car_instance_ids:
            return False
    
        car_dict = {str(i): cid for i, cid in enumerate(car_instance_ids)}
        data_json_str = json.dumps(car_dict, ensure_ascii=False)
        url = f"{BASE_URL}/save_slots_collection"
        params = {"key": self.access_key}
        payload = {
            "account_auth": self.auth_token,
            "data": data_json_str
        }
    
        try:
            response = requests.post(url, params=params, json=payload)
            result = response.json()
            return result.get("ok", False)
        except:
            return False
