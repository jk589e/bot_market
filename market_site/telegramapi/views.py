from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from . import api_telegram
from . import db_api
from .db_api import joinCol, chek_user,addUser
from .api_telegram import get_file , get_users_photo
import json, pandas as pd
from pandas import json_normalize
import datetime as dt
from sqlalchemy import create_engine


engine = create_engine(db_api.db_string)


class UpdateBot(APIView):
    def post(self, request):
        # Сюда должны получать сообщения от телеграм и далее обрабатываться ботом
        #print(request)
        res = request.body.decode('UTF-8')

        api_telegram.send_message(chat_id=526697170, message=res)
        #print(res)
        res = json.loads(res)
        df = json_normalize(res)
        dfMain = pd.DataFrame(data=[],
                              columns=["update_id", "message_id", "user_name", "first_name", "last_name",
                                       "inlinequery_id", "callbackquery_id", "message_from_id",
                                       "message_chat_id", "message_text", "message_date", "latitude", "longitude"])
        if df.__len__() > 0:  # if new messages exist
            joinCol(dfMain, "update_id", df, "update_id")
            joinCol(dfMain, "message_id", df, "message.message_id")
            joinCol(dfMain, "message_from_id", df, "message.from.id")
            joinCol(dfMain, "message_chat_id", df, "message.chat.id")
            joinCol(dfMain, "user_name", df, "message.chat.username")
            joinCol(dfMain, "first_name", df, "message.chat.first_name")
            joinCol(dfMain, "last_name", df, "message.chat.last_name")
            joinCol(dfMain, "message_text", df, "message.text")
            joinCol(dfMain, "message_date", df, "message.date")
            joinCol(dfMain, "latitude", df, "message.location.latitude")
            joinCol(dfMain, "longitude", df, "message.location.longitude")
            try:
                dfMain["message_date"] = pd.to_datetime(dfMain['message_date'], unit='s') + dt.timedelta(hours=3)
            except:
                pass
            #print(dfMain)
            dfMain.to_sql(name='market_telegramlog', con=engine, schema='public', if_exists='append',
                          index=False)  # write log to database

        if chek_user(dfMain.iloc[0,7]) == 0:

            try:
                request = get_users_photo(user_id = dfMain.iloc[0,7])
                res = request.text
                res = json.loads(res)
                df = json_normalize(res["result"]["photos"][0])
                file_id = df.iloc[1, 0]

                get_file(file_id=file_id, user_id=  dfMain.iloc[0,7])
            except: api_telegram.send_message(chat_id=526697170, message='ошибочка')
            addUser(dfAddUser=dfMain.loc[[0], ["user_name", "message_from_id", "first_name", "last_name",
                                     "message_date"]],user_id=dfMain.iloc[0,7])  # ['user_name', 'message_from_id', 'first_name', 'last_name', 'message_date']
            api_telegram.send_message(chat_id=526697170, message=str(dfMain.iloc[0,7]))
        api_telegram.send_message(chat_id=dfMain.iloc[0,7], message=str(dfMain.iloc[0,9]))

        return Response({'code': 200})
