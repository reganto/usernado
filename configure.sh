#!/bin/bash

mkdir -p ~/.usernado
if [ -d "~/.usernado" ]; then
    rm -r ~/.usernado/*
fi
mv ../usernado ~/.usernado/

mv usernado /bin/
rm configure.sh
