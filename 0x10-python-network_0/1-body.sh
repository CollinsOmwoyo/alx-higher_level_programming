#!/bin/bash
# take in a URL, sends a request to that URL, body of the response
curl -sX GET $1 -L
