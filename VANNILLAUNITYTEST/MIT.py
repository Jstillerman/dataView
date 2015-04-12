import os, time

def send(url):
	#PATH = "./DataViewLinux.x86_64 &"
	#PATH = "Untitled.app/Contents/MacOS/Untitled &"
	PATH = "DataView_win_DirectToRift &"

	file = open('settings.temp', 'w+')

	file.write(url)

	time.sleep(1)

	file.close()


	os.system(PATH)
