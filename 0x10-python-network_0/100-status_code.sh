#!/bin/bash
# sends a request to a URL passed
curl -o /dev/null -sw "%{http_code}" $1
