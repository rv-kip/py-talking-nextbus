py-talking-nextbus
==================

## Summary
OS X command line utility to keep you informed verbally of buses arriving at your favorite stop.
Nextbus API documentation is here: http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf

## Installation
Git clone this repo.

## Usage
This only works on OS X with text-to-speech capability.

### Help
```
$ python talking-nextbus.py  --help
Usage: talking-nextbus.py [options]

Options:
  -h, --help            show this help message and exit
  -a AGENCY, --agency=AGENCY
                        Name of the transit agency (default:"sf-muni")
  -c COMMAND, --command=COMMAND
                        Command to execute (routeList|prediction)
  -r ROUTETAG, --route_tag=ROUTETAG
                        The route identifier (Ex: 67, N, J)
  -s STOPID, --stop_id=STOPID
                        The stop ID for the route (Ex: 14159)
```
### Get Agency List
```
$ python talking-nextbus.py -c agencyList
California-Northern
    Unitrans ASUCD/City of Davis (Unitrans)          unitrans
    AC Transit                                       actransit
    Emery-Go-Round                                   emery
    San Francisco Muni (SF Muni)                     sf-muni
California-Southern
    Thousand Oaks Transit (TOT) (Thousand Oaks Transit) thousand-oaks
...
```
### Get Route List
```
$ python talking-nextbus.py  -a sf-muni -c routeList
E-Line                       E
F-Market & Wharves           F
J-Church                     J
KT-Ingleside/Third Street    KT
L-Taraval                    L
M-Ocean View                 M
N-Judah                      N
...
```
### Get Bus Prediction
```
$ python talking-nextbus.py  -a sf-muni -r 67 -s 14159
```
The script will read off a list of the buses arriving at that stop in the near future.
