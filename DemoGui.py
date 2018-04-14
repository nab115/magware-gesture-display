from tkinter import *
import time
 
window = Tk()
readFile = open("/home/michael/Git/wrist-controller-app/cmake-build-debug/current_gesture.txt", "r")
window.title("Welcome to MagWare Event Viewer!")
window.geometry('400x100')
gesture = 0
new_gesture = 0
scroll_mode = False
lbl = Label(window, text="Begin!", font=("Courier", 44))
lbl.grid(column=0, row=0)
window.update()
time.sleep(2)
lbl.config(text="")
window.update()
window.update()
time.sleep(1)


while True :
	token = readFile.read();
	if token != "": 
		new_gesture = int(token);
		if(new_gesture == 1):
			lbl.config(text="Left Click")
			window.update()
			time.sleep(1.5)
			lbl.config(text="")
		if(new_gesture == 2):
			lbl.config(text="Right Click")
			window.update()
			time.sleep(1.5)
			lbl.config(text="")
		if(new_gesture == 3):
			lbl.config(text="Scroll Mode")
		if(new_gesture == 4):
			lbl.config(text="")
			
	window.update()
	readFile.seek(0, 0)
	gesture = new_gesture
	time.sleep(0.1)
