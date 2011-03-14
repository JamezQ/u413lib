from u413lib import parse_chat
from BeautifulSoup import BeautifulStoneSoup
a = open('parse.txt').read()
b = parse_chat(a)
def extra_parse(string):
	string=unicode(BeautifulStoneSoup(string,convertEntities=BeautifulStoneSoup.HTML_ENTITIES ))
	return string
for message in b['GENERAL']:
	print repr(message['Msg'])
