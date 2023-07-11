import vk_api
from pprint import pprint
from course import *
import requests

xml_2 = "https://swapi.dev/api/planets/"

def get_planets():
    return xml_2.find(max(int("diemeter")))

def get_starships():
    response = requests.get("https://swapi.dev/api/starships/") 
    return response.json()

token = 'vk1.a.mMWT43dyKOVPJkBYLq5Vuk1pVR3ZjzuPtX16oxLwEl_HX_gVbZ7nf8AfktqTEj2qrvTLD8SHcDuMbk2iYUI4MfrJeLucDWjvrr_YSWMihKHjN5nQgZ-QLCLiX775fwej5QVsqDCqMOk-vvLZA3wx2keANrY-W4gK6oPrp5o-bFNYZFUTEtl5YiJsXnpXxriu2s3TuByKtzxKxchJIa-Neg'

vk = vk_api.VkApi(token = token)

vk._auth_token()



while True:

    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    pprint(messages)
    if messages['count'] != 0:
        msg = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']
        msg_id = messages['items'][0]['last_message']['id']
        if msg.lower == 'курс':
            vk.method('messages.send', {'user_id': user_id, 'random_id': msg_id, 'message': get_course('R01235')})
            print(get_course('R01235'))  
        elif msg.lower == 'корабли':
            starships = get_starships()["results"] 
            fastest_starship = max(starships, key=lambda x: int(x["max_atmosphering_speed"])) 
            response = f'Максимальная скорость звездного корабля {fastest_starship["name"]} - {fastest_starship["max_atmosphering_speed"]} км/ч.'  
        elif msg.lower == 'планеты':
            vk.method('messages.send', {'user_id': user_id, 'random_id': msg_id, 'message': get_planets("results".xml_2)})
            print(get_planets())
        else:
            vk.method('messages.send', {'user_id':user_id, 'random_id': msg_id, 'message': msg})