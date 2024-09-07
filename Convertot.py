from NumberSystem import Converter as NCon

NCon = NCon()

validBase = ["RGB", "CMYK"]
validEx = ["CMYK", "RGB"]

def ParseData():
	base_type = input("Chose base color system (RGB, CMYK, HSV, HEX): ")
	ex_type = input("Chose finaly color system (RGB, CMYK, HSV, HEX): ")

	if base_type == "RGB" and ex_type == "CMYK":
		R = input("R: ")
		G = input("G: ")
		B = input("B: ")

		R = int(R)
		G = int(G) 
		B = int(B)

		if R > 255 or B > 255 or G > 255:
			print("Invalid data!")
			return

		C, M, Y, K = rgb2cmyk(R, G, B)
		print(f"SMYK: ({C}, {M}, {Y}, {K})")

	if base_type == "CMYK" and ex_type == "RGB":
		print("Okay. Enter the data")
		C = int(input("C: "))
		M = int(input("M: "))
		Y = int(input("Y: "))
		K = int(input("K: "))

		R, G, B = cmyk2rgb(C, M, Y, K, integ)

		print(f"Your resault is: ({R}, {G}, {B})")

	if base_type == "RGB" and ex_type == "HSV":
		print("Okay. Enter the data")

		R = int(input("R: "))
		G = int(input("G: "))
		B = int(input("B: "))

		H, S, V = rgb2hsv(R, G, B)

		print(f"Your resault is: ({H}°, {S}%, {V}%)")

	if base_type == "HSV" and ex_type == "RGB":
		print("Okay. Enter the data")

		H = int(input("H: "))
		S = int(input("S: "))
		V = int(input("V: "))

		R, G, B = hsv2rgb(H, S, V)

		print(f"Your resault is: ({R}, {G}, {B})")

	if base_type == "RGB" and ex_type == "HEX":
		print("Okay. Enter the data")

		R = int(input("R: "))
		G = int(input("G: "))
		B = int(input("B: "))

		HEX = rgb2hex(R, G, B)

		print(f"Hex: {HEX}")

	if base_type == "CMYK" and ex_type == "HSV":
		print("Okay. Enter data")

		C = int(input("C: "))
		M = int(input("M: "))
		Y = int(input("Y: "))
		K = int(input("K: "))

		H, S, V = cmyk2hsv(C, M, Y, K)

		print(f"Your resault is: ({H}, {S}, {V})")

	# if base_type == "CMYK" and ex_type == "HEX":
	# 	print("Okay. Enter data")

	# 	C = int(input("C: "))
	# 	M = int(input("M: "))
	# 	Y = int(input("Y: "))
	# 	K = int(input("K: "))

	# 	HEX = cmyk2hex(C, M, Y, K)

	# 	print(f"Your resault is: {HEX}")
		#---------------------------------------------------------------------------------

	if base_type == "CMYK" and ex_type == "HEX":
		print("Okay. Enter data")

		C = int(input("C: "))
		M = int(input("M: "))
		Y = int(input("Y: "))
		K = int(input("K: "))

		HEX = cmyk2hex(C, M, Y, K)

		print(f"Your resault is: ({HEX})")

	if base_type == "HSV" and ex_type == "HEX":
		print("Okay. Enter data")

		H = int(input("H: "))
		S = int(input("S: "))
		V = int(input("V: "))

		HEX = hsv2hex(H, S, V)

		print(f"Your resault is: ({HEX})")

	if base_type == "HEX" and ex_type == "CMYK":
		print("Okay. Enter data")

		HEX = input("HEX :").replace("#", "")

		C, M, Y, K = hex2cmyk(HEX)

		print(f"Your resault is: ({C} {M} {Y} {K})")

	if base_type == "HEX" and ex_type == "HSV":
		print("Okay. Enter data")

		HEX = input("HEX :").replace("#", "")

		H, S, V = hex2hsv(HEX)

		print(f"Your resault is: ({H} {S} {V})")


def rgb2cmyk(R, G, B, integ=True):
	Rh = R/255
	Gh = G/255
	Bh = B/255

	K = 1 - max(Rh, Gh, Bh)

	C = (1 - Rh - K) / (1 - K) * 100
	M = (1 - Gh - K) / (1 - K) * 100
	Y = (1 - Bh - K) / (1 - K) * 100

	K = K * 100

	if integ:
		C = int(C)
		M = int(M)
		Y = int(Y)
		K = int(K)

	return (C, M, Y, K)


def cmyk2rgb(C, M, Y, K, integ=True):
	C = C/100
	M = M/100
	Y = Y/100
	K = K / 100

	R = 255 * (1 - C) * (1 - K)
	G = 255 * (1 - M) * (1 - K)
	B = 255 * (1 - Y) * (1 - K)

	if integ:
		R = int(R)
		G = int(G)
		B = int(B)

	return (R, G, B)


def rgb2hsv(R, G , B, integ=True):
	Rh = R / 255
	Gh = G / 255
	Bh = B / 255

	Cmax = max(Rh, Gh, Bh)
	Cmin = min(Rh, Gh, Bh)

	deltC = Cmax - Cmin

	Hh = 0 			#Init Hh
	if deltC == 0:
		Hh = None
	if Cmax == Rh:
		Hh = ( (Gh - Bh) / deltC ) % 6
	if Cmax == Gh:
		Hh = ( (Bh - Rh) / deltC ) + 2
	if Cmax == Bh:
		Hh = ( (Rh - Gh) / deltC ) + 4

	H = 60 * Hh

	S = 0
	if Cmax == 0:
		S = 0
	else:
		S = deltC / Cmax

	V = Cmax

	S = S * 100
	V = V * 100

	if integ:
		H = int(H)
		S = int(S)
		V = int(V)

	return (H, S, V)


def hsv2rgb(H, S, V, integ=True):
	S = S / 100
	V = V / 100

	C = S * V
	Hh = H / 60

	X = C * ( 1 - abs(Hh % 2 - 1) )
	def GetRGBh(Hh, C, X):
		if Hh == None:
			return (0, 0, 0)
		if Hh >= 0 and Hh < 1:
			return (C, X, 0)
		if Hh >= 1 and Hh < 2:
			return (X, C, 0)
		if Hh >= 2 and Hh < 3:
			return (0, C, X)
		if Hh >= 3 and Hh < 4:
			return (0, X, C)
		if Hh >= 4 and Hh < 5:
			return (X, 0, C)
		if Hh >= 5 and Hh < 6:
			return (C, 0, X)

	Rh, Gh, Bh = GetRGBh(Hh, C, X)
	m = V - C
	R, G, B = ((Rh + m) * 255, (Gh + m) * 255, (Bh + m) * 255) 

	if R < 0 : R = 0
	if G < 0 : G = 0 
	if B < 0 : B = 0 

	if integ:
		R, G, B = (int(R), int(G), int(B))

	return (R, G, B)


def rgb2hex(R, G, B):
	Rh = NCon.dec2hex(R)
	Gh = NCon.dec2hex(G)
	Bh = NCon.dec2hex(B)

	RGBh = [Rh, Gh, Bh]
	# print(RGBh)
	HEX = ()

	for x in RGBh:
		if len(x) != 2:
			x = f"0{x}"
		if x == "" or x =="0":
			x = "00"
		HEX += (x,)	

	HEX_S = "#"
	for el in HEX:
		HEX_S += el

	return HEX_S


def hex2rgb(HEX):
	Rhex = HEX[0:2]
	Ghex = HEX[2:4]
	Bhex = HEX[4:6]

	R = NCon.hex2dec(Rhex)
	G = NCon.hex2dec(Ghex)
	B = NCon.hex2dec(Bhex)

	return (R, G, B)


def cmyk2hsv(C, M, Y, K):
	R, G, B = cmyk2rgb(C, M, Y, K)
	H, S, V = rgb2hsv(R, G, B)
	return (H, S, V)


def cmyk2hex(C, M, Y, K):
	R, G, B = cmyk2rgb(C, M, Y, K)
	return rgb2hex(R, G, B)


def hsv2hex(H, S, V):
	R, G, B = hsv2rgb(H, S, V)
	return rgb2hex(R, G, B)


def hex2cmyk(HEX):
	R, G, B = hex2rgb(HEX)
	return rgb2cmyk(R, G, B)


def hex2hsv(HEX):
	R, G, B = hex2rgb(HEX)
	return rgb2hsv(R, G, B)


if __name__ == '__main__':
	while True:
		ParseData()
	# print(rgb2hex(0,0,59))
