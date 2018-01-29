#!/usr/bin/python3

'''

function:
get a 8-digits birthday as an input,
out the corresponding life code

'''


def code_add(code1, code2):
	code_sum = code1 + code2
	while code_sum >= 10:
		code1 = code_sum % 10
		code2 = code_sum // 10
		code_sum = code1 + code2
	return code_sum

def birth_to_life_code(birthday):
	
	#assert input birthday format is correct
	assert birthday > 10**7 and birthday < 10**8 and birthday % 100 <= 31 and birthday % 100 > 0 and birthday // 100 % 100 <= 12 and birthday // 100 % 100 >0

	#transfer birthday into 8 single num in list code
	code = []
	for i in range(8):
		code.append(birthday%10)
		birthday //= 10
	
	#apply life code rule to get lifeCode
	codeD = code_add(code[0],code[1])
	codeM = code_add(code[2],code[3])
	codeY2 = code_add(code[4],code[5])
	codeY1 = code_add(code[6],code[7])
	codeDM = code_add(codeD, codeM)
	codeYY = code_add(codeY1, codeY2)
	codeLife = code_add(codeDM, codeYY)

	return codeLife
		

birthday = input("请输入您的出生年月日，格式如： 19920625 \n")

while True:

	try:
		#calculate life code and print
		codeLife = birth_to_life_code(int(birthday))
		print("您的生命密码为 %s" %codeLife)
		break
		
	except:
		birthday = input("您的输入格式有误，正确的八位数字年月日的格式如： 19900130 \n请重新输入: \n")
	
