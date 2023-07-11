import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from pprint import pprint
from course import *
from random import randint
from wiki import *

token = 'vk1.a.mMWT43dyKOVPJkBYLq5Vuk1pVR3ZjzuPtX16oxLwEl_HX_gVbZ7nf8AfktqTEj2qrvTLD8SHcDuMbk2iYUI4MfrJeLucDWjvrr_YSWMihKHjN5nQgZ-QLCLiX775fwej5QVsqDCqMOk-vvLZA3wx2keANrY-W4gK6oPrp5o-bFNYZFUTEtl5YiJsXnpXxriu2s3TuByKtzxKxchJIa-Neg'

vk_session = vk_api.VkApi(token = token)

vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        msg_id = randint(1, 10 ** 7)
        print(msg)
        if msg[2:] == '-к ':
            res = f'{msg} = {get_course_2(msg)}'
        elif msg.startswith('-в'):
            res = get_wiki_article(msg[3:])
        else:
            res = 'Не понимаю, что ты хочешь'
        vk.messages.send(user_id = user_id, random_id = msg_id, message = res)
        print(res)