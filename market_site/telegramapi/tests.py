import json, pandas as pd
from market_site.telegramapi.api_telegram import get_users_photo as gt, get_file
from pandas.io.json import json_normalize
# Create your tests here.
request = gt(526697170)
res = request.text
res = json.loads(res)
df = json_normalize(res["result"]["photos"][0])
file_id = df.iloc[1,0]

get_file(file_id = file_id, user_id=526697170)


#print(file_path["result"]["file_path"])




