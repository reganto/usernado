#!/bin/bash

if [ -d "~/.tornado" ]
then 
    rm -r ~/.tornado/
else
    mv ../tornado/ ~/.tornado/
fi

mv tornado /bin/
rm configure.sh
