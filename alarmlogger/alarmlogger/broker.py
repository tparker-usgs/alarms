import json

from .db import Db

def callback(ch, method, properties, body):
    conn = Db('/alarms')

    data = json.loads(body)
#        with open("image.jpg","wb") as fout:
#            fout.write(base64.b64decode(data['file']))

    print("New alarm:");
    print("volcano: {}".format(data['volcano']))
    print("subject: {}".format(data['subject']))
    print("message: {}".format(data['message']))
    print("\n\n");
    conn.insert_alarm(data)

