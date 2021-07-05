tabla={'1': ' ', '2': ' ', '3': ' ',
       '4': ' ', '5': ' ', '6': ' ',
       '7': ' ', '8': ' ', '9': ' '}

def afisare(tabla):
    print('|'+tabla['1']+'|'+tabla['2']+'|'+tabla['3']+'|')
    print('--+-+--')
    print('|'+tabla['4']+'|'+tabla['5']+'|'+tabla['6']+'|')
    print('--+-+--')
    print('|'+tabla['7']+'|'+tabla['8']+'|'+tabla['9']+'|')
    print('--+-+--')

def joace():
    player1='X'
    player2='0'
    counter=0
    for i in range(10):
        afisare(tabla)
        if(i%2==0):
            print("Player 2 please introduce your position:")
        else:
            print("Player 1 please introduce your position:")
        position=input()
        if tabla[position]==' ' and i%2==0:
            tabla[position]=player2
            counter+=1
        elif tabla[position]==' ' and i%2!=0:
            tabla[position]=player1
            counter+=1
        else:
            print("This place is full\n")
            continue
        if counter>=5:
            if tabla['1']==tabla['2']==tabla['3']=='X' and tabla['1']==tabla['2']==tabla['3']!=' ':
                afisare(tabla)
                print("\n Player 1 won\n")
                break
            elif tabla['1']==tabla['2']==tabla['3']=='0' and tabla['1']==tabla['2']==tabla['3']!=' ':
                afisare(tabla)
                print("\n Player 2 won\n")
                break
            elif tabla['4']==tabla['5']==tabla['6']=='X' and tabla['4']==tabla['5']==tabla['6']!=' ':
                afisare(tabla)
                print("\n Player 1 won\n")
                break
            elif tabla['4']==tabla['5']==tabla['6']=='0' and tabla['4']==tabla['5']==tabla['6']!=' ':
                afisare(tabla)
                print("\n Player 2 won\n")
                break
            elif tabla['7']==tabla['8']==tabla['9']=='X' and tabla['7']==tabla['8']==tabla['9']!=' ':
                afisare(tabla)
                print("\n Player 1 won\n")
                break
            elif tabla['7']==tabla['8']==tabla['9']=='0' and tabla['7']==tabla['8']==tabla['9']!=' ':
                afisare(tabla)
                print("\n Player 2 won\n")
                break
            elif tabla['1']==tabla['4']==tabla['7']=='X' and tabla['1']==tabla['4']==tabla['7']!=' ':
                afisare(tabla)
                print("\n Player 1 won\n")
                break
            elif tabla['1']==tabla['4']==tabla['7']=='0' and tabla['1']==tabla['4']==tabla['7']!=' ':
                afisare(tabla)
                print("\n Player 2 won\n")
                break
            elif tabla['2']==tabla['5']==tabla['8']=='X' and tabla['2']==tabla['5']==tabla['8']!=' ':
                afisare(tabla)
                print("\n Player 1 won\n")
                break
            elif tabla['2']==tabla['5']==tabla['8']=='0' and tabla['2']==tabla['5']==tabla['8']!=' ':
                afisare(tabla)
                print("\n Player 2 won\n")
                break
            elif tabla['3']==tabla['6']==tabla['9']=='X' and tabla['3']==tabla['6']==tabla['9']!=' ' :
                afisare(tabla)
                print("\n Player 1 won\n")
                break
            elif tabla['3']==tabla['6']==tabla['9']=='0' and tabla['3']==tabla['6']==tabla['9']!=' ':
                afisare(tabla)
                print("\n Player 2 won\n")
                break
            elif tabla['1']==tabla['5']==tabla['9']=='X' and tabla['1']==tabla['5']==tabla['9']!=' ':
                afisare(tabla)
                print("\n Player 1 won\n")
                break
            elif tabla['1']==tabla['5']==tabla['9']=='0' and tabla['1']==tabla['5']==tabla['9']!=' ':
                afisare(tabla)
                print("\n Player 2 won\n")
                break
            elif tabla['3']==tabla['5']==tabla['7']=='X' and tabla['3']==tabla['5']==tabla['7']!=' ':
                afisare(tabla)
                print("\n Player 1 won\n")
                break
            elif tabla['3']==tabla['5']==tabla['7']=='0' and tabla['3']==tabla['5']==tabla['7']!=' ':
                afisare(tabla)
                print("\n Player 2 won\n")
                break
        if counter==9:
            print("It's a Tie!!\n")
joace()