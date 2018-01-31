from jinja2 import Environment, PackageLoader, select_autoescape
from .db import Db
import logging
import os
import paramiko
from io import StringIO


def write():
    conn = Db()
    alarms = conn.get_alarms()
    print("TOMP SAYS", alarms)
    render(alarms)
    ship_file()

def render(alarms):
    env = Environment(
        loader=PackageLoader('alarmlogger', 'templates'),
        #autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('alarmlog.html')

    with open('avobroker1.html', 'w') as f:
        f.write( template.render( alarms=alarms ) )


def ship_file():
    print("TOMP SAYS SHIPPING FILE")

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.getLogger().setLevel(logging.DEBUG)

    # Open a transport
    transport = paramiko.Transport((os.environ['WEB_HOST']))

    # Auth
    pkey = paramiko.RSAKey.from_private_key(StringIO(os.environ['PRIVATE_KEY'].replace('\\n', '\n')))
    user = os.environ['USER']
    transport.connect(pkey = pkey, username = user)

    # Go!
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Upload
    filepath = os.environ['WEB_PATH'] + 'avobroker1.html'
    localpath = 'avobroker1.html'
    sftp.put(localpath, filepath)

    # Close
    sftp.close()
    transport.close()
