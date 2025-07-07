
# aileens_musing# Aileen Novero 
## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 

Let's go back to basics for another moment, Shell scripting .. 

## 
> A shell script comprises the following elements –
* Keywords - if else break ...
* Cmds  - ls cd echo pwn touch ...
* Functions - if... then... else; case; loops
* Fourth item

> Why
* AUTOMATE! 
* Routine backups for system admin
* System monitoring
> Advantages
* command line syntax
* quick starts
* debugging
> Disadvantages
* Slow
* Not optimal for large tasks
* Minimal structure
* Design flaws 
* Easy to cause a costly error

```sh x.sh
#!/bin/bash
#
echo "Back to basics ->  Bash tutorial: http://linuxconfig.org/Bash_scripting_Tutorial"
```
###### make sure to change permissions :) 
```sh
chmod +x x.sh
```

__ 
> A word about variables
A variable name could contain any alphabet (a-z, A-Z), any digits (0-9), and an underscore ( _ ). Howver, it can never START with a number; Note: There should not be any space around the “=” sign in the variable assignment. When you use VariableName=value, the shell treats the “=” as an assignment operator and assigns the value to the variable. When you use VariableName = value, the shell assumes that VariableName is the name of a command and tries to execute it.


`$PWD` = Stores working directory 

`$HOME` = Stores user's home directory

`$SHELL` = Stores the path to the shell program that is being used.

```sh
#!
var1="KnightOfNi"
echo $var1

unset var1

if [ -z $var1 ]; then
  echo "You unset it correctly"
fi
```

> A note on controls
>> looping
```sh
#/bin/bash
while <condition>
do
    <command 1>
    <command 2>
    <etc>
done
```

>> if else then
```sh
#/bin/bash
if [ expression ]
then
   statement1
else
   statement2
fi
```

