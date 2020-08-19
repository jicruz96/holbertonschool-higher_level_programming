#!/bin/bash
# Sends a request to inputted URL; displays size of body of response
curl -sI $1 | grep Content-Length | cut -d' ' -f2
