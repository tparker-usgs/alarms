import json

from .db import Db
from .writer import write

def callback(ch, method, properties, body):
    alarm = parse_alarm(body)
    print_message(alarm)
    insert_alarm(alarm)
    
    write()

def parse_alarm(body):
    alarm = json.loads(body)
    #with open("image.jpg","wb") as fout:
        #fout.write(base64.b64decode(alarm['file']))
    return alarm

def insert_alarm(alarm):
    conn = Db()
    conn.insert_alarm(alarm)
    
def print_message(alarm):
    print("New alarm:");
    print("volcano: {}".format(alarm['volcano']))
    print("subject: {}".format(alarm['subject']))
    print("message: {}".format(alarm['message']))
    print("\n\n");
