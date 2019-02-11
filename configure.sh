#!/bin/bash

if [ -d "~/.tornado/tornado" ]
then 
    rm -r ~/.tornado/tornado
else
    mv ../tornado/ ~/.tornado/
fi

mv tornado /bin/
rm configure.sh
