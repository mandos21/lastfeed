#!/bin/sh


# Source colors from my wal colorscheme

. "${HOME}/.cache/wal/colors.sh"


~/lastfeed/wrapper.sh | lemonbar -g 1920x20+3840 -b -B "$color0" -F "$color1" -U "$color1" -p -u 3
