#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -o /dev/null -sw "You find me!" 0.0.0.0:5000/catch_me
