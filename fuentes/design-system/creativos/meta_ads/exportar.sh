#!/bin/zsh
# Exporta cada HTML a PNG con el Chrome instalado:
#   01..10  → pack-renova/meta-ads/            (feed, 1080×1350)
#   h_01..  → pack-renova/meta-ads/historias/  (historias y reels, 1080×1920)
cd "$(dirname "$0")"; OUT=../../../../pack-renova/meta-ads; mkdir -p $OUT/historias
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
shot(){ "$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=4000 \
    --screenshot="$PWD/$2" --window-size=$3 "file://$PWD/$1" >/dev/null 2>&1 }
for f in [0-9]*.html; do shot $f $OUT/${f%.html}.png 1080,1350; done
for f in h_*.html; do n=${f#h_}; shot $f $OUT/historias/${n%.html}_9x16.png 1080,1920; done
ls $OUT/historias
