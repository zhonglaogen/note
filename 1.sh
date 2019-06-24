#!/bin/bash

#add
num=10
i=0
while $i -le $num
do
num=`expr $i + $num`
i=`expr $i + 1`
done
echo $num
