from Tkinter import *
import time
 
window = Tk()
readFile = open("Gestures.txt", "r")
window.title("Welcome to MagWare Event Viewer!")
window.geometry('400x100')
gesture = 0
new_gesture = 0
scroll_mode = 0
lbl = Label(window, text="Begin!", font=("Courier", 44))
lbl.grid(column=0, row=0)
window.update_idletasks()
window.update()
time.sleep(2)
lbl.config(text="")
window.update_idletasks()
window.update()
window.update()
time.sleep(1)


while True :
	new_gesture = int(readFile.read())
	if(gesture == 0 and new_gesture != 0):
		if(new_gesture == 1):
			lbl.config(text="Left Click")
			window.update_idletasks()
			window.update()
			time.sleep(1.5)
			lbl.config(text="")
		if(new_gesture == 2):
			lbl.config(text="Right Click")
			window.update_idletasks()
			window.update()
			time.sleep(1.5)
			lbl.config(text="")
		if(new_gesture == 3):
			lbl.config(text="Scroll Mode")
			window.update_idletasks()
			window.update()
	window.update_idletasks()
	window.update()
	readFile.seek(0, 0)
	gesture = new_gesture
	time.sleep(0.1)