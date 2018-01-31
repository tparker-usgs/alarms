docker stop alarmlogger
docker rm alarmlogger
docker build -t alarmlogger .
docker run --detach=true --env-file=/home/tparker/private/alarmlogger.env --name alarmlogger alarmlogger
docker ps
docker logs alarmlogger
