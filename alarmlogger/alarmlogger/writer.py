from jinja2 import Environment, PackageLoader, select_autoescape
from .db import Db
import os
import paramiko



def write():
    conn = Db()
    alarms = conn.get_alarms()
    print("TOMP SAYS", alarms)
    render(alarms)
    ship_file()

def render(alarms):
    env = Environment(
        loader=PackageLoader('alarmlogger', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('alarmlog.html')

    with open('avobroker1.html', 'w') as f:
        f.write( template.render( alarms=alarms ) )


def ship_file():
    #paramiko.util.log_to_file('/tmp/paramiko.log')

    # Open a transport
    transport = paramiko.Transport((os.environ['WEB_HOST']))

    # Auth
    hostkey = os.environ['WEB_HOST_KEY']
    pkey = os.environ['PRIVATE_KEY']
    transport.connect(hostkey = hostkey, pkey = pkey)

    # Go!
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Upload
    filepath = '/home/avobroker1.html'
    localpath = '/home/avobroker1.html'
    sftp.put(localpath, filepath)

    # Close
    sftp.close()
    transport.close()
