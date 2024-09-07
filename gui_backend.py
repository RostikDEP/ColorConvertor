import Convertot
import tkinter
print(Convertot.rgb2hex(234,24,24))

class Backend:
	def __init__(self,label , R, G, B):
		self.R = R 
		self.G = G
		self.B = B
		self.label = label


	def InitLables(self, rgb, cmyk, hsv, hex_):
		self.labelRGB = rgb
		self.labelCMYK = cmyk
		self.labelHSV = hsv
		self.labelHEX = hex_


	def UpdateValues(self):
		self.labelRGB.set(f"RGB: ({self.R}, {self.G}, {self.B})")

		CMYK = Convertot.rgb2cmyk(int(self.R), int(self.G), int(self.B))
		self.labelCMYK.set(f"CMYK: {CMYK}")

		HSV = Convertot.rgb2hsv(int(self.R), int(self.G), int(self.B))
		self.labelHSV.set(f"HSV: {HSV}")

		HEX = Convertot.rgb2hex(int(self.R), int(self.G), int(self.B))
		self.labelHEX.set(f"HEX: {HEX}")


	def ChangeLabelColor(self):
		self.label.config(bg=Convertot.rgb2hex(int(self.R), int(self.G), int(self.B)))


	def ValueChangedR(self, value):
		self.R = value
		print((self.R, self.G, self.B))
		self.ChangeLabelColor()
		self.UpdateValues()


	def ValueChangedG(self, value):
		self.G = value
		print((self.R, self.G, self.B))
		self.ChangeLabelColor()
		self.UpdateValues()


	def ValueChangedB(self, value):
		self.B = value
		print((self.R, self.G, self.B))
		self.ChangeLabelColor()
		self.UpdateValues()