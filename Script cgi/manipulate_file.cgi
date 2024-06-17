#!/bin/bash

echo "Content-type: text/html"
echo ""

echo "<html><body>"
echo "<h1>Contenu du Fichier</h1>"
echo "<pre>"
cat /usr/lib/cgi-bin/script.php
echo "Bonjour, ceci est une ligne ajoutée par le script CGI" >> /usr/lib/cgi-bin/script.php
echo "</pre>"
echo "</body></html>"
