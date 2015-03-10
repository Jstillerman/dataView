from Tkinter import *
import requests
import MIT


class App:
    default_names=('delpwr', 'wnpar',  'spsi', 'ws', 'wr', 'wz', 'wphi')
    start_sample="1"
    end_sample="50"
    start_ray="1"
    end_ray= "5"

    def onselect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        active = w.get(index)
        try:
        	self.download(self.entry.get()+ "/" + active)
        	self.entry.insert(END, "/" + active)
        except Exception, e:
        	print e, "didn't work"

    def slide1(self, value):
    	if(self.w.get() >= self.x.get()):
    		self.x.set(self.w.get()+1)
    	if(self.y.get() >= self.z.get()):
    		self.z.set(self.y.get()+1)
    	self.start_ray=str(self.w.get())
    	self.end_ray=str(self.x.get())
    	self.start_sample=str(self.y.get())
    	self.end_sample=str(self.z.get())
    def slide2(self, value):
    	if(self.w.get() >= self.x.get()):
    		self.w.set(self.x.get()-1)
    	if(self.y.get() >= self.z.get()):
    		self.y.set(self.z.get()-1)
    	self.start_ray=str(self.w.get())
    	self.end_ray=str(self.x.get())
    	self.start_sample=str(self.y.get())
    	self.end_sample=str(self.z.get())
    def getMeta(self, url):
		variables = requests.get(url + "?meta=yes").json()
		for thing in variables['Vars']:
			self.extraNames.insert(END, thing)
	

	

    def __init__(self, master):
    	frame = Frame(master)
    	frame.pack()
    	self.secret = frame

	scrollbar = Scrollbar(master)
	scrollbar.pack(side=LEFT, fill=Y)

	
	self.listbox = Listbox(master, yscrollcommand=scrollbar.set, width=70)
	self.listbox.pack(side=LEFT, fill=BOTH)
	
	self.listbox.bind('<Double-Button-1>', self.onselect)
#START/END RAYS
	Label(master, text="Starting\nRay").pack(side=LEFT)
	self.w = Scale(master, from_=1, to=9, command=self.slide1)
	self.w.pack(side=LEFT)
	Label(master, text="Ending\nRay").pack(side=LEFT)
	self.x = Scale(master, from_=2, to=10, command=self.slide2)
	self.x.pack(side=LEFT)
#START/END SAMPLES
	Label(master, text="Starting\nSample").pack(side=LEFT)
	self.y = Scale(master, from_=1, to=99, command=self.slide1)
	self.y.pack(side=LEFT)
	Label(master, text="Ending\nSample").pack(side=LEFT)
	self.z = Scale(master, from_=2, to=100, command=self.slide2)
	self.z.pack(side=LEFT)



	self.nameManager = Listbox(master, width=30)
	self.nameManager.pack(side=BOTTOM, fill=BOTH)
	self.nameManager.bind('<Double-Button-1>', self.removeName)

	self.extraNames = Listbox(master, width=30)
	self.extraNames.pack(side=LEFT, fill=BOTH)
	self.extraNames.bind('<Double-Button-1>', self.addName)

	for name in self.default_names:
		self.nameManager.insert(END, name)
	
	self.entry = Entry(frame, width=50)
	self.entry.pack(side=LEFT)
	self.entry.insert(0, "http://127.0.0.1:5000/data/home")

	self.entryGET = Entry(frame, width=20)
	self.entryGET.pack(side=LEFT)
	self.entryGET.insert(0, "?key=hi")

	self.hi_there = Button(frame, text="Download", command= lambda: self.download(self.entry.get()))
	self.hi_there.pack(side=LEFT)

	self.metaButton = Button(frame, text="Download Meta", command= lambda: self.getMeta(self.entry.get()))
	self.metaButton.pack(side=LEFT)

	self.rift = Button(frame, text="Send to Rift", command= self.send)
	self.rift.pack(side=LEFT)
	self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
	self.button.pack(side=LEFT)



	

    def download(self, url):
    	files = requests.get(url + self.entryGET.get()).json()
    	self.listbox.delete(0, END)
    	for file in files["Files"]:
    		self.listbox.insert(END, file)
    	

    def removeName(self, evt):
    	w= evt.widget
    	index = int(w.curselection()[0])
    	self.extraNames.insert(END, w.get(index))
    	w.delete(ANCHOR)

    def addName(self, evt):
    	w= evt.widget
    	index = int(w.curselection()[0])
    	self.nameManager.insert(END, w.get(index))
    	w.delete(ANCHOR)

	
    def send(self):
    	theNames = ""
    	for i in range(0, self.nameManager.size()):
    		theNames += self.nameManager.get(i) + "%20"
    	print theNames
    	extra = ("&firstray="+self.start_ray+"&lastray="+self.end_ray+"&firstsample="+self.start_sample+"&lastsample="+self.end_sample+"&names="+theNames)
    	print "SENDING URL", self.entry.get() + self.entryGET.get() + "&doSend=yes" + extra
    	MIT.doodad(self.entry.get() + self.entryGET.get() + "&doSend=yes" + extra)




root = Tk()

app = App(root)

root.mainloop()
root.destroy() 
