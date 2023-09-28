#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the body of the response if status is 200
curl -sL "$1"
