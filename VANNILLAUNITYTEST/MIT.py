import os, time

def doodad(url):
	#PATH = "./DataViewLinux.x86_64 &"
	#PATH = "Untitled.app/Contents/MacOS/Untitled &"
	PATH = "DataView_win_DirectToRift &"
	print """
	 __      __       .__
	/  \    /  \ ____ |  |   ____  ____   _____   ____
	\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \
	 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/
	  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
	       \/       \/          \/            \/     \/
	       """

	file = open('settings.temp', 'w+')

	file.write(url)

	time.sleep(1)

	file.close()


	os.system(PATH)
