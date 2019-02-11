#!/bin/bash

if [ -d "~/.tornado/tornado" ]
    rm -r ~/.tornado/tornado
else
    mv ../tornado/ ~/.tornado/
fi

mv tornado /bin/
rm configure.sh

cd ~

