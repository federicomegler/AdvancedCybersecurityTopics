from subprocess import run

flag = "flag{packer_asul_coolg+6$defghij}"
output = run(["./john",flag], capture_output=True).stdout
if output == b'\x1b[1;31mLoser\n\x1b[0m':
	print(flag)





your_list = 'abcdefghijklmnopqrstuvwxyz_'
complete_list = []
for current in range(10):
	a = [i for i in your_list]
	for y in range(current):
        	a = [x+i for i in your_list for x in a]
	flag = "flag{" + a + "}"
	output = run(["./john",flag], capture_output=True).stdout
	if output != b'\x1b[1;31mLoser\n\x1b[0m':
		print(flag)
		break
    
