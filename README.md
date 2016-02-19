MassScanner
==============

## SUMMARY

A tool for creating an IP address list by several parameters.
You can choose the ports that must be open, checked whether they are honeypots, ...

## USAGE


```
$ chmod+x MassScanner.py && ./MassScanner.py
```

## COMMANDS

help: this dialog
exit: quit MassScanner
generate <filename> [ip range: 82-83.0-255.0-255.0.255]: generate ip list from a range (default: 5.0.0.0 to 5.255.255.255)
port <filename> <output> <port>: generate open port ip list from another ip list
alive <filename> <output>: generate alive ip list from another ip list
hpot <type: kippo> <filename> <output>: generate a list with only honeypots ip
rpot <type: kippo> <filename> <output>: generate a list without honeypots ip

## TODO

-Multithreading
-More honeypots detector
-Multi port ip

## DISCLAIMER

Don't be an asshole. I take no responsibility for how you use this. It's not even that cool so you should probably use someone else's code.
