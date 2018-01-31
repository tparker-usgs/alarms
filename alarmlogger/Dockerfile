# log alarm messages
#
# BUILD-USING:  docker build -t alarmlogger .
# RUN-USING:    docker run --detach=true --name alarmlogger alarmlogger
#

# can't use onbuild due to SSL visibility
FROM python:3

WORKDIR /root/.pip
ADD pip.conf .

#RUN apt-get -y install vim

WORKDIR /root/certs
add DOIRootCA2.cer .

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#1
COPY . .

CMD [ "python", "./alarmlogger.py" ]
