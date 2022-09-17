rgb = input().casefold().replace("rgb(","").replace(")","").split(",")
string = bytearray()
for i in rgb:
	string.append(int(i.strip()))
print("#%s" %string.hex())