
import requests as rq
import pandas as pd
import json
from pandas.io.json import json_normalize
from . import db_api

from django.conf import settings



base_url = "https://api.telegram.org/bot"
#bot_token = "5285834737:AAEQ5sIkdX2bdcAd6HQSjN1xzemp5UyMxgA"
bot_token = "5353508249:AAEwYhk4JJVKgKxRAlsthZtmwdE26BrpJ-c"
api_url= base_url + bot_token

def joinCol(A,a,B,b):
    try:
        A[a]=B[b]
    except: pass



def get_updates():
    offset = db_api.get_offset()
    jsonbody = '{"offset":'+str(offset)+',"allowed_updates":["message","edited_message","callback_query","inline_query","chosen_inline_result"]}'
    headers = {'content-type': 'application/json'}
    res = rq.post(api_url + '/getUpdates', data=jsonbody, headers=headers, verify=False)

    res = json.loads(res.text)
    # print(res)
    df = json_normalize(res["result"])

    return df

def send_message(chat_id,message):
    headers = {'content-type': 'application/json'}
    body = {"chat_id": str(chat_id), "text": message}
    rq.post(api_url + '/sendMessage', json=body, headers=headers, verify=False)

def get_users_photo(user_id):
    headers =headers = {'content-type': 'application/json'}
    body = {"user_id": str(user_id),"limit" : "3"}
    #res_photo = rq.get(api_url + '/getUserProfilePhotos', json=body, headers=headers, verify=False)
    res_photo = rq.get(api_url + '/getUserProfilePhotos?user_id='+str(user_id)+'&limit=1', headers=headers, verify=False)
    return res_photo

def get_file(file_id, user_id):
    headers = {'content-type': 'application/json'}
    body = {"file_id": str(file_id)}
    file_res = rq.get(api_url + '/getFile', json=body, headers=headers, verify=False)
    file_path = json.loads(file_res.text)
    file_path = file_path["result"]["file_path"]
    url = 'https://api.telegram.org/file/bot' + bot_token +'/'+ file_path
    response = rq.get(url)
    open( settings.MEDIA_ROOT +'/userphotos/' + str(user_id)+'.jpg','wb').write(response.content)



