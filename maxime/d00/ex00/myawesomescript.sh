#!/bin/bash

curl $1 2>&1 | grep 'moved here' | cut -d \" -f 2
