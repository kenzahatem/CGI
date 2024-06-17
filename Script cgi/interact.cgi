#!/bin/bash

echo "Content-type: text/html"
echo ""

echo "<html><body>"
echo "<h1>Utilisation du Disque</h1>"
echo "<pre>"
df -h
echo "</pre>"
echo "</body></html>"
