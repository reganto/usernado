#!/bin/bash

if [ ! -d "~/.usernado" ]
then 
    mkdir -p ~/.usernado
    mv ../usernado/ ~/.usernado/usernado
else
    rm -rf ~/.usernado/*
    mv ../usernado/ ~/.usernado/usernado
fi

mv usernado /bin/
rm configure.sh
