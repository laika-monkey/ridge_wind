#!/bin/bash

ARCHIVE=/mnt/media/data/weather/nhc_adv

for YR in {2019..2010}; do
for N_STM in {01..30}; do
	NDIR=$ARCHIVE/$YR/AT${N_STM}/
	mkdir -p $NDIR
        cd $NDIR	
for ADV in {001..100}; do
	FILENAME=AL${N_STM}${YR}_${ADV}adv_CONE.kmz
	if [ ! -f $FILENAME ]; then
		URL=http://www.nhc.noaa.gov/storm_graphics/api/$FILENAME
		echo $URL
		wget $URL
	fi
	FILENAME=AL${N_STM}${YR}_${ADV}adv_TRACK.kmz
	if [ ! -f $FILENAME ]; then
		URL=http://www.nhc.noaa.gov/storm_graphics/api/$FILENAME
		echo $URL
		wget $URL
	fi
	if [[ $? > 0 ]]; then
		break
	fi
done; done; done

rm -vrf `find $ARCHIVE/ -type d -empty` 
