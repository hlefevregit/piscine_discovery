#!/bin/bash

if [ $# -eq 0 ]; then
	echo "No arguments supplied"
	exit 1
else
	for i; do
		if [ $i -lt 1 ] || [ $i -gt 5 ]; then
			break
		fi
		echo $i
	done
fi

