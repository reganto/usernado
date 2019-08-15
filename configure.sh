#!/bin/bash

if [ -d "~/.usernado/" ]
then 
    rm -rf ~/.usernado/*
    mv ../usernado/ ~/.usernado/
else
    mkdir ~/.usernado
    mv ../usernado/ ~/.usernado/
fi

mv usernado /bin/
rm configure.sh
