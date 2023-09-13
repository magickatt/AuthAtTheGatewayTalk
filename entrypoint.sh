#!/bin/bash

# https://www.baeldung.com/linux/check-variable-exists-in-list
function exists_in_list() {
    LIST=$1
    DELIMITER=$2
    VALUE=$3
    LIST_WHITESPACES=`echo $LIST | tr "$DELIMITER" " "`
    for x in $LIST_WHITESPACES; do
        if [ "$x" = "$VALUE" ]; then
            return 0
        fi
    done
    return 1
}

# Simple way to validate the entrypoint argument
valid_flask_apps="api-with-auth api-without-auth standalone-auth":
if exists_in_list "$valid_flask_apps" " " $1; then
    flask --app $1 run --host=0.0.0.0
else
    echo "Please use a valid Flask app [api-with-auth|api-without-auth|standalone-auth]"
    exit 1
fi
