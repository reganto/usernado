#!/bin/bash

mkdir -p ~/.usernado
cp -rf ../usernado ~/.usernado/

mv ~/.usernado/usernado/usernado /bin/
rm ~/.usernado/usernado/configure.sh
