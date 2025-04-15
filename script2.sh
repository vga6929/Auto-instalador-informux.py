#!/bin/bash

mkdir -p  /data/data/com.termux/files/usr/bin/informux

cp desktop-dark /data/data/com.termux/files/usr/bin/informux

chmod +x /data/data/com.termux/files/usr/bin/informux/desktop-dark

echo "export PATH=\$PATH:/data/data/com.termux/files/usr/bin/informux/" >> /data/data/com.termux/files/usr/etc/bash.bashrc

source /data/data/com.termux/files/usr/etc/bash.bashrc
