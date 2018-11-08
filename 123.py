password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	pw = input ('Please enter password: ')
	if pw != password:
		print ('wrong password!you still have', i,'chance(s)')
		if i == 0:
			print ('wrong password!')
			break
	else:
		print ('password correct!')
		break
