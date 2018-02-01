docker stop alarmlogger
docker rm alarmlogger
docker build -t alarmlogger .
docker run --detach=true --env-file=/home/tparker/private/alarmlogger.env --name alarmlogger alarmlogger
docker ps
sleep 2
docker logs alarmlogger
