#!/bin/bash
# URL as an argument, GET request to the URL, and display response
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
