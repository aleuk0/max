def a():
    print("OK!")

while(True):
    inp = input("just print something \n" )
    message = inp.split(" ")
    if message[0] == 'a':
        a()

    elif message[0] == 'exit':
        break
    
