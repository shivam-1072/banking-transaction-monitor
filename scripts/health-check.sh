#!/bin/bash

URL="http://localhost:5000"

STATUS="(curl -o /dev/null -s -w "%{http_code}" $URL)

if [ $STATUS -eq 200]
then 
    echo "Application is Healthy"
else
    echo "Application is Down"
fi