def hi() :
	print('Hi there!')
	print('How are you?')
hi()
hi()
hi()

if 3 > 2:
	print('It works!')

if 5 > 2:
	print('5 est effectivement plus grand que 2')
else:
	print("5 n'est pas plus grand que 2")
	
def hi(name):

	print('Hi ' + name + '!')
	
hi("Rachel")

def hi(name):
	print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
	hi(name)
	print('Next girl')

