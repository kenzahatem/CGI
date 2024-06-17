#!/bin/bash

echo "Content-type: text/html"
echo ""

read -n $CONTENT_LENGTH POST_DATA

echo "<html><body>"
echo "<h1>Résultats du Formulaire</h1>"
echo "<p>Données reçues : $POST_DATA</p>"

# Extraire les paramètres
NOM=$(echo "$POST_DATA" | sed -n 's/^.*nom=\([^&]*\).*$/\1/p' | sed 's/%20/>AGE=$(echo "$POST_DATA" | sed -n 's/^.*age=\([^&]*\).*$/\1/p')

echo "<p>Nom : $NOM</p>"
echo "<p>Âge : $AGE</p>"
echo "</body></html>"


