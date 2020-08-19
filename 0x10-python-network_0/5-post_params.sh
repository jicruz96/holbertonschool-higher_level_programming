#!/bin/bash
# sends a POST req. to URL with an email and subject, displays body of response
subject="I will always be here for PLD"
email="hr@holbertonschool.com"
curl -s -X POST -d "email=$email" -d "subject=$subject" $1
