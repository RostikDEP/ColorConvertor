from tkinter import *
from gui_backend import Backend

root = Tk()
root.geometry('300x220')

labelColor = Label(root, bg="#ff0000", height=2, width=40)
Backend = Backend(labelColor, 0,0,0)
labelColor.pack()

scaleR = Scale(root,
	 			from_=0,
	 			to=255, 
	 			resolution=1,
	 			orient=HORIZONTAL,
	 			width=10,
	 			length=300,
	 			bg="#ffe8e8",
	 			command=Backend.ValueChangedR
	 			)
scaleR.pack()

scaleG = Scale(root,
	 			from_=0,
	 			to=255, 
	 			resolution=1,
	 			orient=HORIZONTAL,
	 			width=10,
	 			length=300,
	 			bg="#d9ffdf",
	 			command=Backend.ValueChangedG
	 			)
scaleG.pack()

scaleB = Scale(root,
	 			from_=0,
	 			to=255, 
	 			resolution=1,
	 			orient=HORIZONTAL,
	 			width=10,
	 			length=300,
	 			bg="#d7d7fa",
	 			command=Backend.ValueChangedB
	 			)
scaleB.pack()

textRGB  = StringVar()
textCMYK = StringVar()
textHSV = StringVar()
textHEX = StringVar()

textRGB.set("RGB")
textCMYK.set("CMYK")
textHSV.set("HSV")
textHEX.set("HEX")

labelRGB = Entry(root, textvariable = textRGB)
labelCMYK = Entry(root, textvariable = textCMYK)
labelHSV = Entry(root, textvariable = textHSV)
labelHEX = Entry(root, textvariable = textHEX)

labelRGB .pack()
labelCMYK.pack()
labelHSV .pack()
labelHEX .pack()

Backend.InitLables(textRGB, textCMYK, textHSV, textHEX)

root.mainloop()