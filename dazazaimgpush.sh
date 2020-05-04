#!/bin/bash
echo '--- git push start'
echo “arg1 = $1” 
echo '----------------------------------'
git add "$1"
git commit -m 'update by py'
git push
echo '--- git push done'
echo '----------------------------------'