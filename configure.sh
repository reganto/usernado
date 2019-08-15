#!/bin/bash

if [ ! -d "~/.usernado" ]
then 
    mkdir ~/.usernado
    mv ../usernado/ ~/.usernado/usernado
else
    rm -rf ~/.usernado/*
    mv ../usernado/ ~/.usernado/usernado
fi

mv usernado /bin/
rm configure.sh
