import sys;
import urllib.request;
import codecs;
import xml.etree.ElementTree as ET;

elementToFind = sys.argv[1];

url = 'https://configsa01.blob.core.windows.net/rfm/rfmOnAir.xml';
filename = '/config/www/downloads/rfm.xml';

urllib.request.urlretrieve(url, filename);
with codecs.open(filename, 'r', encoding='utf16') as f: text = f.read();
with codecs.open(filename, 'w', encoding='utf8') as f: f.write(text);

root = ET.fromstring(text);

for name in root.iter(elementToFind):
    print(name.text)