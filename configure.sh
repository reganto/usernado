#!/bin/bash

if [ -d "~/.usernado" ]
then 
    rm -rf ~/.usernado/
else
    mv ../usernado/ ~/.usernado/
fi

mv usernado /bin/
rm configure.sh
