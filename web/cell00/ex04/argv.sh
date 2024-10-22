#!/bin/bash

if [ $# -eq 0 ]; then
	echo "No arguments supplied"
	exit 1
else
	for i; do
		echo $i
	done
fi

