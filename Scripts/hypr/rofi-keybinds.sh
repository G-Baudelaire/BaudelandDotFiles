#!/bin/bash

hyprctl binds -j |
  python ~/Scripts/hypr/rofi_keybinds.py -i -j |
  rofi -dmenu -markup-rows -i |
  sed -n 's/.*<span color=\"cyan\">\(.*\)<\/span>.*/\1/p' |
  sed -e 's/^/"/g' -e 's/$/"/g' |
  xargs -n1 hyprctl dispatch
