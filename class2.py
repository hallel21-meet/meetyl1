list1 = [8, 5, 9]
list2 = [7, 4, 5, 8]

def common_num (hey,you):
	God = []
	for num in hey:
		if num in you:
			God.append(num)
	return(God)
mai = common_num(list1, list2)
print(mai)
print(sum(mai))

encoder_caesar= {'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p'}