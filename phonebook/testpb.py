def add():
    print("OK!")
	
def exit():
	...

while(True):
    inp = input("just print something \n" )
    message = inp.split(" ")
    if message[0] == '��������':
        add()
	#��� ���������� �������� ������ ���������� pep-0263

    elif message[0] == 'exit':
        break
    
