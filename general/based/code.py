from tkinter import S


def showmenu():
    print("menu:")
    print("1. binary to ascii")
    print("2. decimal to ascii")
    print("3. hex to ascii")
    print("anything else = stop the program")

    menu = input("choose: ")
    match menu:
        case '1':
            binary = input("binary: ")
            conv = binary.split()
            s = ''.join(conv)
            print(''.join(chr(int(s[i*8:i*8+8], 2)) for i in range(len(s)//8)))
            return 
            
        case '2':
            oct = input("oct: ")
            conv = oct.split()
            s = ''
            for i in range(len(conv)):
                s += chr(int(conv[i],8))
            print(s)
            return
            
        case '3':
            hex = input("hex: ")
            conv = hex.split()
            s = ''.join(conv)
            byte_string = bytes.fromhex(s)
            print(byte_string.decode('utf-8'))
            return
        
        case _:
            return False

stop = True
while stop:
    stop = showmenu()
