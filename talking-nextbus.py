#!/usr/bin/env python
import time
import string
import urllib
from xml.dom import minidom
import os
from optparse import OptionParser

baseUrl = "http://webservices.nextbus.com/service/publicXMLFeed"

def initOptions():
    parser = OptionParser()
    parser.add_option("-a", "--agency",
                      dest="agency",
                      help="Name of the transit agency (default:\"sf-munu\")",
                      default="sf-muni",
                      # default="muni",
                      )
    parser.add_option("-c", "--command",
                      dest="command",
                      default="predictions",
                      help="Command to execute (routeList|prediction)",
                      )
    parser.add_option("-r", "--route_tag",
                    dest="routeTag",
                    default="67",
                    help="The route identifier (Ex: 67, N, J)",
                    )
    parser.add_option("-s", "--stop_id",
                    dest="stopId",
                    default="14159",
                    help="The stop ID for the route (Ex: 14159)",
                    )
    (options, args) = parser.parse_args()
    return options

def getXmlFromUrl (url):
    data = urllib.urlopen(url).read();
    xmlData = minidom.parseString(data)
    # TODO: handle XML error here
    return xmlData

def pad(count):
    padding = ""
    for i in range (1, count):
        padding+=" "
    return padding

# Replace various bits to make the TTS comprehensible
def englishIfy(text):
    replaceMap = { " & "        : " and ",
                   " Ave"          : " Avenue",
                   " St"          : " Street"  }

    for key in replaceMap.keys():
        text = string.replace(text, key, replaceMap[key])

    return text

# Convert bus info into human readable/speakable text
def busInfoToText (xml):
    routeTag = xml.getElementsByTagName("predictions")[0].getAttribute("routeTag")
    stopTitle = xml.getElementsByTagName("predictions")[0].getAttribute("stopTitle")

    stopTitle = englishIfy(stopTitle)

    info = "Predictions for the " + str(routeTag) + " bus at " + stopTitle
    return info

def getRouteList(params):
    col_width = 30
    url = baseUrl + "?command=" + params.command + "&a=" + params.agency
    print(url)
    xmlData = getXmlFromUrl(url)
    routes = xmlData.getElementsByTagName("route")
    for route in routes:
        title = route.getAttribute("title")
        routeTag =route.getAttribute("tag")
        print title + pad(col_width - len(title)) + routeTag

def getBusInfo (params):
    url = baseUrl + "?command=" + params.command + "&a=" + params.agency + "&stopId=" + params.stopId + "&r=" + params.routeTag
    print(url)
    xmlData = getXmlFromUrl(url)
    text = busInfoToText(xmlData)
    speakTextOSX(text)

    # drill down to predictions
    predicts = xmlData.getElementsByTagName("prediction");
    num_of_predicts = predicts.length
    speakTextOSX("I found " + str(num_of_predicts) + " predictions.")

    prediction_times = []

    for prediction in predicts:
        prediction_times.append(prediction.getAttribute("minutes"))

    for ptime in prediction_times:
        ptime = str(ptime)
        time_units = "minutes"
        if (ptime == "1"):
            time_units = "minute"
        speakTextOSX(ptime + " " + time_units)
        time.sleep(0.5)

def speakTextOSX(text):
    os.system("say " + text)

def main ():
    options = initOptions()

    if (options.command == "routeList"):
        getRouteList(options)
    elif (options.command == "predictions"):
        getBusInfo(options)
    else:
        print "Invalid command parameter:" + options.command

if __name__ == "__main__":
    # Someone is launching this directly
    main()
