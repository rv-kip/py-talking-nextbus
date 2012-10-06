py-talking-nextbus
==================

## Summary
OS X command line utility to keep you informed verbally of buses arriving at your favorite stop.

## Usage
This only works on OS X with text-to-speech capability

```
$ python talking-nextbus.py  --help
Usage: talking-nextbus.py [options]

Options:
  -h, --help            show this help message and exit
  -a AGENCY, --agency=AGENCY
                        Name of the transit agency (default:"sf-munu")
  -c COMMAND, --command=COMMAND
                        Command to execute (routeList|prediction)
  -r ROUTETAG, --route_tag=ROUTETAG
                        The route identifier (Ex: 67, N, J)
  -s STOPID, --stop_id=STOPID
                        The stop ID for the route (Ex: 14159)
```

```
$ python talking-nextbus.py  -a sf-muni -r 67 -s 14159
```
The script will read off a list of the buses arriving at that stop in the near future.
