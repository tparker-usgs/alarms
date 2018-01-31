from jinja2 import Environment, PackageLoader, select_autoescape
from .db import Db



def write():
    conn = Db()
    alarms = conn.get_alarms()
    print("TOMP SAYS", alarms)
    render(alarms)
 

def render(alarms):
    env = Environment(
        loader=PackageLoader('alarmlogger', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('alarmlog.html')

    with open('avobroker1.html', 'w') as f:
        f.write( template.render( alarms ) )
