import sys;
import json;
from urllib.request import urlopen;

elementToFind = sys.argv[1];

numberOfArgs = len(sys.argv);

if numberOfArgs == 3:
    sencondLevel = sys.argv[2];

antena3 = "https://www.rtp.pt/play/livechannelonair.php?channel=1&howmanynext=0&howmanybefore=0&channeltype=radio";

jsonString = urlopen(antena3);
antena3Json = jsonString.read();
antena3 = json.loads(antena3Json);

if numberOfArgs == 2:
    elementValue = antena3['raw']['result'][0]['onair'][0][elementToFind];

if numberOfArgs == 3:
    elementValue = antena3['raw']['result'][0]['onair'][0][elementToFind][sencondLevel];

print(elementValue);