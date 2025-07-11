#!/bin/bash

#
echo "Back to basics ->  Bash tutorial: http://linuxconfig.org/Bash_scripting_Tutorial"
#To print length of string inside Bash Shell: '#' symbol is used to print the length of a string.
var1="KnightOfNi"
echo $var1
echo "length of var1 and substring part" ${#var1} ${var1:8}

#concantentate strings
varlong=$var1$var1$var1
echo $varlong
varlong=$var1***$var1
echo $varlong
#To create an array, print an array and length
arr=("value1" value2 $var1)
echo ${arr[@]} "length" ${#arr[@]}


unset var1 varlong

if [ -z $var1 ]; then
  echo "You unset it correctly"
fi
