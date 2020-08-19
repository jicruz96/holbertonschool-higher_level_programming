#!/bin/bash
# displays allowed HTTP methods for server at URL
curl -sI $1 | grep Allow | cut -d':' -f2 | cut -d' ' -f2-
