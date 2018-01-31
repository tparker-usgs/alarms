from .db import Db

def write():
    conn = Db()
    alarms = conn.get_alarms()
    print("TOMP SAYS", alarms)
 

