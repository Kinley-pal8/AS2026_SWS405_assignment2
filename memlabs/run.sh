#!/bin/bash
# usage: run.sh <lab#> <profile> plugin [plugin...]  -> out/labN_<plugin>.txt
n=$1; p=$2; shift 2; cd /home/kp/Desktop/SWS405/SWS405_a2/memlabs/Lab$n
for pl in "$@"; do volatility --plugins=$HOME/volatility-plugins -f MemoryDump_Lab$n.raw --profile=$p $pl > ../out/lab${n}_$pl.txt 2>&1 & done; wait
