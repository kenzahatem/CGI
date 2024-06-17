#!/bin/bash

echo "Content-type: text/html"
echo ""

echo "<html><body>"
echo "<h1>Variables d'Environnement CGI</h1>"
echo "<pre>"
env
echo "</pre>"
echo "</body></html>"
