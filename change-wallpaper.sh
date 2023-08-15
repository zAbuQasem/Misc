#!/bin/bash

WP_FILE=$HOME/.config/wallpaper.jpg
category=$1

wget -q -O "$WP_FILE" https://source.unsplash.com/1920x1080/?$category

if [[ -f "${WP_FILE}" ]]; then
    feh --no-fehbg --bg-fill "$WP_FILE" && \
        notify-send -i emblem-photos "Wallpaper" "Wallpaper changed" \
        -h int:suppress-sound:1 -h int:transient:1
    #wal -i $WP_FILE
fi
