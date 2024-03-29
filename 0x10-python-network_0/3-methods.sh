#!/bin/bash
# A script that displays all HTTP methods the server will accept
allow_header=$(curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-)
echo "$allow_header"
