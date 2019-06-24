#!/bin/bash
num=3
i=0
result=0
while [ $i -le $num ]
 do
  echo "11123"
  result=`expr $result + $i`
  i=`expr $i + 1`
 done

echo "$result"
echo "===================1======================"
num=3
i=0
result=0
while [ $i -le $num ]
 do
  echo "11123"
  let result=$result+$i
  let i=$i+1
 done

echo "$result"
echo "===================2======================"
num=3
i=0
result=0
while [ $i -le $num ]
 do
  echo "11123"
  let "result=$result+$i"
  let "i=$i+1"
 done

echo "$result"
echo "====================3====================="
num=3
i=0
result=0
while [ $i -le $num ]
 do
  echo "11123"
  ((result=$result+$i))
  ((i=$i+1))
 done

echo "$result"
echo "====================4====================="
num=3
i=0
result=0
while [ $i -le $num ]
 do
  echo "11123"
  result=$[$result+$i]
  let i=$[$i+1]
 done

echo "$result"
echo "====================5====================="
num=3
i=0
result=0
while test $i -le $num 
 do
  echo "11123"
  result=$[$result+$i]
  let i=$[$i+1]
 done

echo "$result"

