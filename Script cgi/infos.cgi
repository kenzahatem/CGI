#!/bin/bash

echo "Content-type: text/html"
echo ""

echo "<html><body>"
echo "<h1>Informations CGI</h1>"
echo "<pre>"
echo "REQUEST_METHOD: $REQUEST_METHOD"
echo "CONTENT_LENGTH: $CONTENT_LENGTH"
echo "QUERY_STRING: $QUERY_STRING"
echo "REMOTE_ADDR: $REMOTE_ADDR"
echo "REMOTE_HOST: $REMOTE_HOST"
echo "SERVER_NAME: $SERVER_NAME"
echo "SERVER_PORT: $SERVER_PORT"
echo "SCRIPT_NAME: $SCRIPT_NAME"
echo "SCRIPT_FILENAME: $SCRIPT_FILENAME"

echo "</pre>"
echo "</body></html>"
