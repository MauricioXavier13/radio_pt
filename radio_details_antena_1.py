import sys;
import json;
from urllib.request import urlopen;

elementToFind = sys.argv[1];

antena1 = "https://www.rtp.pt/play/livechannelonairnow.php?channel=at1";

jsonString = urlopen(antena1);
antena1Json = jsonString.read();
antena1 = json.loads(antena1Json);

elementValue = antena1[0]['depg'][elementToFind];

print(elementValue);