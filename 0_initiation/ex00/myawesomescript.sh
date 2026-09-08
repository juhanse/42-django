#!/bin/sh

curl -sIL $1 | grep -i "Location:" | tail -n 1 | awk '{print $2}'