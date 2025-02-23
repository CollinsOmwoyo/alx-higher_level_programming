#!/bin/bash
# takes in a URL and displays
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
