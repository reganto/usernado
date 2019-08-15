#!/bin/bash

mkdir -p ~/.usernado
rm -r ~/.usernado/*
mv ../usernado ~/.usernado/

mv usernado /bin/
rm configure.sh
