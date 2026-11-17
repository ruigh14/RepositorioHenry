#!/bin/zsh
# Exporta cada HTML a PNG de 1080×1350 con el Chrome instalado → pack-renova/meta-ads/
cd "$(dirname "$0")"; OUT=../../../../pack-renova/meta-ads; mkdir -p $OUT
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in [0-9]*.html; do
  "$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=4000 \
    --screenshot="$PWD/$OUT/${f%.html}.png" --window-size=1080,1350 "file://$PWD/$f" >/dev/null 2>&1
done
ls $OUT
