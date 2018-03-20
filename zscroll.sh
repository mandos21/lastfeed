#!/usr/bin/env sh

while true; do
	python3 ~/Nextcloud/Programs/PyScrobbler/scrobblefeed2.py | zscroll  -l 400 -n true -d 0.3 -t 300
	#echo " " | zscroll -l 400 -n true -d 0.3 -t 1
done
