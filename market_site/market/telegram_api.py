
import requests as rq

from django.conf import settings



base_url = "https://api.telegram.org/bot"
#bot_token = "5285834737:AAEQ5sIkdX2bdcAd6HQSjN1xzemp5UyMxgA"
bot_token = "5353508249:AAEwYhk4JJVKgKxRAlsthZtmwdE26BrpJ-c"
api_url= base_url + bot_token






def send_message(chat_id,message):
    headers = {'content-type': 'application/json'}
    body = {"chat_id": str(chat_id), "text": message}
    rq.post(api_url + '/sendMessage', json=body, headers=headers, verify=False)





