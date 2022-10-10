def main():
    a = 0
    while a <= 7:
        b = a + 1
        while b <= 8:
            c = b + 1
            while c <= 9:
                if a != 7:
                    print(str(a), str(b), str(c), ", ", sep='', end='')
                else:
                    print(str(a), str(b), str(c), sep='')
                c += 1
            b += 1
        a += 1


while True:
    yes = input("play again press enter or q to leave").lower()
    if yes == 'q':
        quit()
    else:
        main( )
