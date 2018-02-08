~/bin/protoc --proto_path=src --js_out=library=alarm,binary:js src/alarm.proto 
~/bin/protoc --python_out=../alarmlogger/alarmlogger src/alarm.proto 
