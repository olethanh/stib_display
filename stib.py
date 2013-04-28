import urllib2
import BeautifulSoup
from collections import OrderedDict as odict


station_led = [
    u'trone',
    u'science',
    u'luxembourg',
    u'idalie',
    u'blyckaerts',
    u'germoir',
    u'rodin',
    u'delporte',
    u'etterbeek gare',
]

def get_stations():
    url_heiligenborre = "http://m.stib.be/linelight.php?line=95&iti=1&lang=fr"
    page = urllib2.urlopen(url_heiligenborre).read()
    soup = BeautifulSoup.BeautifulSoup(page)
    return odict([(li.text.lower(), dict(li.attrs).get('class') == 'active') for li in soup('li')])


def leds_from_stations(r):
    return [station_led.index(k) for k,v in r.iteritems() if v and k in station_led]

if __name__ == "__main__":
    stations = get_stations()

    print [k for k,v in stations.iteritems() if v]
    print station_led

    leds = leds_from_stations(stations)
    print leds


