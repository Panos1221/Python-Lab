#-*-coding: utf-8-*-

import sys

f = open(sys.argv[1], "r")
thes = f.read()
f.close()

thesi = 0

mnhmh = [0]
thesimnhm = 0

while thesi < len(thes):
	if thes[thesi] == ">":
		thesimnhm += 1
		if len(mnhmh) <= thesimnhm:
			mnhmh.append(0)
			
	elif thes[thesi] == "<":
		thesimnhm -= 1
		if thesimnhm < 0:
			print("Error: Out of Limit")
			sys.exit(0)
		
	elif thes[thesi] == "+":
		mnhmh[thesimnhm] += 1
		if mnhmh[thesimnhm] >= 255:
			mnhmh[thesimnhm] = 0
		
	elif thes[thesi] == "-":
		mnhmh[thesimnhm] -= 1
		if mnhmh[thesimnhm] <= -1:
			mnhmh[thesimnhm] = 255
		
	elif thes[thesi] == ".":
		print(chr(mnhmh[thesimnhm]), end="")
		
	elif thes[thesi] == ",":
		inp = input("Input requested: ")
		mnhmh[thesimnhm] = ord( inp[0] )
		
	elif thes[thesi] == "[":
		if mnhmh[thesimnhm] == 0:
			countOpened = 0
			thesi += 1
			while thesi < len(thes):
				if thes[thesi] == "]" and countOpened == 0:
					break
				elif thes[thesi] == "[":
					countOpened += 1
				elif thes[thesi] == "]":
					countOpened -= 1
				thesi += 1
				
	elif thes[thesi] == "]":
		if mnhmh[thesimnhm] != 0:
			countClosed = 0
			thesi -= 1
			while thesi >= 0:
				if thes[thesi] == "[" and countClosed == 0:
					break
				elif thes[thesi] == "]":
					countClosed += 1
				elif thes[thesi] == "[":
					countClosed -= 1
				thesi -= 1

	thesi += 1
	
print("")

