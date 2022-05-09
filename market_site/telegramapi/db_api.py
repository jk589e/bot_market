from sqlalchemy import create_engine
import pandas as pd

db_login = "globalvisor"
db_password="Sinhrofazatron1"
db_host = "rc1b-21imrctq167tcobb.mdb.yandexcloud.net"
#db_host = "127.0.0.1"
db_port = "6432"
#db_name = "postgres"
db_name = "telegramlogistics"

db_string = "postgresql://" + db_login + ":" + db_password + "@" + db_host + ":" + db_port + "/" + db_name

engine = create_engine(db_string)

def joinCol(A,a,B,b):
    try:
        A[a]=B[b]
    except: pass

def get_offset(): #get the last update_id from log table
    offset = (pd.read_sql_query('select max(update_id) from public.market_telegramlog', con=engine)).iloc[0,0]

    if offset == None:
        offset = 0
    else:
        offset = offset+1

    return offset

def processed(update_id): #flag current log message
    sql = ''' update public.market_telegramlog
              set processed=1 
              where update_id= '''+ str(update_id)
    connection = engine.connect()
    connection.execute(sql)

def chek_user(user_id):

    sql = '''
    select user_id from public.market_user where user_id=''' + str(user_id)
    user = pd.read_sql_query(sql,con=engine)
    if len(user)<1:
        res = 0
    else :
        res =1
    return res




def addUser(dfAddUser): # add new user to user tables
    dfAddUser.rename(columns={ 'message_from_id': 'user_id', 'message_date':'first_message_time'},  inplace=True)
    dfAddUser['status']=0
    dfAddUser.to_sql(name='market_user', con=engine, schema='public', if_exists='append', index=None)

def get_replies():
    sql = ''' SELECT 
    	a.update_id, 
    	a.message_id, 
    	a.message_from_id, 
    	a.message_chat_id, 
    	a.inlinequery_id, 
    	a.callbackquery_id, 
    	a.user_name, -- rename
    	a.first_name, 
    	a.last_name, 
    	a.message_text, 
    	a.message_date, 
    	a.latitude, 
    	a.longitude, 
    	a.processed,
    	b.status,
    	null as role_id,
    	null as company_id,
    	null as is_active,
    	null as registration_code
    FROM public.market_telegramlog  a left join public.market_user b on a.message_from_id = b.user_id 
    where a.processed is null
    order by update_id
    limit 1
    '''
    return pd.read_sql_query(sql,con=engine)

def updateStatus(status,chat_id):

    sql = ''' update public.market_user 
                  set status='''+ str(status) + ''' 
                  where user_id= ''' + str(chat_id)
    connection = engine.connect()
    connection.execute(sql)
