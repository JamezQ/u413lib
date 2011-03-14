import u413lib
import time
def main():
	logger = u413lib.createclient()
	logger.login('USER','PASS')
	chatter = logger.joinchat('general')
	
	while True:
		time.sleep(15)
		chat = chatter.get()
		if chat:
			for c in chat:
				c['Unixtime'] = time.time()
				logstring = repr(c)
				logfile = open('chatlog.log','a')
				logfile.write(logstring+"\n")
				logfile.close()
				
	
if __name__ == "__main__":
	main()
