#!/bin/bash
# Make a request to the URL that causes the server to respond with "You got me!"
curl -s -X -L PUT -d "user_id=98" 0.0.0.0:5000/catch_me
