from u413lib import parse_chat
a = open('parse.txt').read()
b = parse_chat(a)
for message in b['GENERAL']:
	print message['Msg']
