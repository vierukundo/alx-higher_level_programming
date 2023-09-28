#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the body of the response if status is 200
if [ $(curl -sI "$1" | awk 'NR==1{print $2}') -eq 200 ]; then curl -s "$1"; fi
