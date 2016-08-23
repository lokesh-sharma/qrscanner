from Tkinter import *
import tkFileDialog as fd
import tkFont
import pyqrcode
import qrtools


class App:
	
	def __init__(self , master):
		
		frame = Frame(master)
		frame.pack()
		self.ins = ("INSTRUCTIONS:\n"
		"TO ENCODE a message:\n"
		"enter message in text field and click encode button on top\n"
		"a png image file will be saved in current dir\n"
		"TO DECODE a QR code :\n"
		"click open and select the image file\n"
		"decoded messsage will be displayed on screen")
		self.background = Label(master , text=self.ins , justify=LEFT)
		self.background.pack()
		self.background.place(x=200,y=200)
		self.cFont = tkFont.Font(family="Helvetica" , size = 12)
		self.text = Entry(master)
		self.heading  = Label(master , text="QR code encoder and decoder	" , font=self.cFont)
		self.input = Label(master , text="enter the message to encode:")
		self.output = Label(master , text="decoded message")
		self.output.pack()
		self.input.pack()
		self.heading.pack()
		self.heading.place(x=0 , y=0)
		self.text.pack()
		self.open = Button(frame , text = "open" , fg="green" , command = self.open_file)
		self.encode = Button(frame , text="encode" , fg = "blue" , command = self.encode_message)
		self.open.pack(side=RIGHT)
		self.encode.pack()

	def open_file(self):
		tempdir = fd.askopenfile()
		qrdecode = qrtools.QR()
		qrdecode.decode(tempdir.name)
		self.output['text'] = qrdecode.data
	def encode_message(self):
		message = self.text.get()
		if(message != ""):
			qr = pyqrcode.create(message)
			qr.png("code" + message[0] + ".png" , scale = 6)
root = Tk()
root.geometry('640x480')
root.title("QR scanner")
app = App(root)
root.resizable(width=False,height=False)
root.mainloop()
root.destroy()
