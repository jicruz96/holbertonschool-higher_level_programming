#!/bin/bash
# sends a POST req. to URL with an email and subject, displays body of response
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
