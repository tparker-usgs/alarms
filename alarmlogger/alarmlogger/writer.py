from jinja2 import Environment, PackageLoader, select_autoescape
from datetime import datetime, timedelta
from .db import Db
import logging
import os
import paramiko
from io import StringIO


def write():
    conn = Db()
    alarms = conn.get_alarms()
    print("TOMP SAYS", alarms)

    day = datetime.now().strftime('_%Y%m%d')
    filename_pattern = os.environ['HOSTNAME'] + '_%Y%m%d.html'
    render(alarms, filename_pattern)
    ship_file(filename_pattern)

def render(alarms, filename_pattern):
    env = Environment(
        loader=PackageLoader('alarmlogger', 'templates'),
        #autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('alarmlog.html')

    now = datetime.now()
    this_file = now.strftime(filename_pattern)

    previous = now - timedelta(days=1)
    previous_file = previous.strftime(filename_pattern)

    next = now + timedelta(days=1)
    next_file = previous.strftime(filename_pattern)

    tmpl_vars = {}
    tmpl_vars['alarms'] = alarms
    tmpl_vars['last_update'] = now.strftime('%x %X')
    tmpl_vars['host'] = os.environ['HOSTNAME']
    tmpl_vars['date'] = now.strftime('%x')
    tmpl_vars['next_file'] = next.strftime(filename_pattern)
    tmpl_vars['previous_file'] = previous.strftime(filename_pattern)
    with open(this_file, 'w') as f:
        f.write(template.render(tmpl_vars))


def ship_file(filename_pattern):
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.getLogger().setLevel(logging.DEBUG)

    transport = paramiko.Transport((os.environ['WEB_HOST']))

    # Auth
    pkey = paramiko.RSAKey.from_private_key(StringIO(os.environ['PRIVATE_KEY'].replace('\\n', '\n')))
    user = os.environ['USER']
    transport.connect(pkey = pkey, username = user)

    # Go!
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Upload
    remote_path = os.environ['WEB_PATH'] + os.environ['HOSTNAME']
    try:
        sftp.chdir(remote_path)
    except IOError:
        sftp.mkdir(remote_path)
        sftp.chdir(remote_path)

    filename = datetime.now().strftime(filename_pattern)
    sftp.put(filename, filename)
    sftp.close()
    transport.close()
