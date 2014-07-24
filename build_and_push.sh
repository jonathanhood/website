#!/bin/bash

make html

git clone https://github.com/jonathanhood/jonathanhood.github.io.git
cp -R output/* jonathanhood.github.io/.
cd jonathanhood.github.io

git config user.name $GIT_NAME
git config user.email $GIT_EMAIL
git config credential.helper "store --file=.git/credentials"
echo 'https://'$GH_TOKEN':@github.com' >> .git/credentials
git add .
git commit -m "Updating with latest changes"
git push

