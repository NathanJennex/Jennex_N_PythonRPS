#check a temperature and output as  result
#
temperature = int (input("input a number between 0 and 100"))

if temperature <= 4:
	print("water is a solid, beacuse it is frozen")

	elif temperature < 100:
		print("water is a liquid")

	else: temperature >=100:
		print("water is a gas, beacuase it is boiling")