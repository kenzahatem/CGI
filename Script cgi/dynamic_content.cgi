#!/bin/bash

echo "Content-type: text/html"
echo ""

echo "<html><body>"
echo "<h1>Contenu Dynamique PHP</h1>"
echo "<pre>"
php /usr/lib/cgi-bin/script.php
echo "</pre>"
echo "</body></html>"
