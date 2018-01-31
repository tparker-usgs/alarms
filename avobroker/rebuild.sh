docker stop avobroker
docker rm avobroker
docker build -t avobroker .

docker run	\
--detach	\
--network=host	\
-p 25672:25672	\
-p 4369:4369	\
-p 15672:15672	\
-p 5672:5672	\
--name avobroker	\
--env-file=/home/tparker/private/avobroker.env \
rabbitmq:3-management

docker ps
docker logs avobroker

# join cluster
# docker exec -it avobroker bash
# rabbitmqctl stop
# rabbitmqctl join_cluster rabbit@avobroker1
# rabbitmqctl start_app
# rabbitmqctl cluster_status
