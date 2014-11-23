#!/bin/bash

PELICAN=/usr/bin/pelican
CONTENT=/home/basepi/Dropbox/Blogs/blog.cmyers.net/content
OUTPUT=/home/basepi/Dropbox/Blogs/blog.cmyers.net/output
SETTINGS=/home/basepi/Dropbox/Blogs/blog.cmyers.net/publishconf.py

rm -rf /home/basepi/Dropbox/Blogs/blog.cmyers.net/output/*
$PELICAN $CONTENT -o $OUTPUT -s $SETTINGS || exit $?
rsync -r --delete /home/basepi/Dropbox/Blogs/blog.cmyers.net/output/ /var/www/blog.cmyers.net
