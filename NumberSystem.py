class Converter:
	def dec2hex(self, decValue):
		if decValue == 0:
			return "0"

		hexN = []
		hexF = []

		converting = True
		while converting:
			divR = decValue // 16
			mult = divR * 16
			sub = decValue - mult

			if sub ==0:
				converting = False
				break
			
			hexN.append(str(sub))
			decValue = divR

		i = 0

		for ln in range(len(hexN)): hexF.append(0)

		for el in hexN:
			el = el.replace("10", "A").replace("11", "B").replace("12", "C")
			el = el.replace("13", "D").replace("14", "E").replace("15", "F")
			ln = len(hexN) - 1
			hexF[ln - i] = el
			i += 1

		hexResault = ""
		for symb in hexF:
			hexResault += symb

		return hexResault


	def hex2dec(self, decValue):
		
		dischHex = []
		numHex = []
		for charIndex in range(len(decValue)):
			dischHex.append(decValue[charIndex])

		for el in dischHex:
			el = el.replace("A", "10").replace("B", "11").replace("C", "12")
			el = el.replace("D", "13").replace("E", "14").replace("F", "15")

			numHex.append(int(el))

		reverseHex = []
		for i in range(len(numHex)): reverseHex.append(None)	

		i = 0
		for el in numHex:
			reverseHex[len(numHex)-1 - i] = el
			i += 1

		decValue = 0
		for x in range(len(reverseHex)):
			decValue += reverseHex[x] * (16 ** x)

		return decValue