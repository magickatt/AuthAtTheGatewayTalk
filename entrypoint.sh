#!/bin/bash

case $1 in

  "api-with-auth")
    echo "Running api-with-auth..."
    flask --app api-with-auth run --host=0.0.0.0 --debug
    ;;

  "api-without-auth")
    echo "Running api-without-auth..."
    flask --app api-without-auth run --host=0.0.0.0 --debug
    ;;

  "standalone-auth")
    echo "Running standalone-auth..."
    python -u standalone-auth.py
    ;;

  *)
    echo "Please use a valid Flask app [api-with-auth|api-without-auth] or HTTPServer standalone-auth"
    exit 1
    ;;

esac
