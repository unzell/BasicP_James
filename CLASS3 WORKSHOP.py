wildBeast = 150
ken = 50
fisticuff = 5
dagger = 20
keizoku = True
damage = 0

def checkBeastHp ():
    global wildBeast, damage

    if wildBeast == 0:
        print("MISSION完了、これから帰還する。")
        wildBeast = 150
    elif wildBeast < 0:
        print("you attacked the wildBeast so much that it regained it strenght\nwildBeast regained its strength\nwildBeast gained 20 HP back !")
        wildBeast += 20

def weaponCode ():
    global wildBeast, damage

    weapon = input("weapon's code (NO UPPERCASE): ")
    if weapon in ["sword", "dagger", "fist"]:
        if weapon == "sword":
            damage = ken
        elif weapon == "dagger":
            damage = dagger
        elif weapon == "fist":
            damage = fisticuff

        wildBeast -= damage 
        print("wildBeast's current HP : ",wildBeast)

        checkBeastHp()

        
    else:
        print("invalid weapon code")
        weaponCode()


while keizoku:
    print("enter 1 to fight wildBeast | 2 to quit")
    option = int(input("option : "))

    if option == 1:
        回数 = int(input("WILDBEASTを攻撃するの回数 : "))
        for i in range(回数):
            if i == len(range(回数)) and wildBeast > 0:
                print("お前の負けだ LOSER")
                wildBeast = 150
            else:
                print("The following is the weapon's code and it's damage")
                print("weapon's damage\nsword : 50\ndagger : 20\nfist : 5")
                weaponCode()
            
            
    elif option == 2:
        print("臆病者。がっかりだわ 😒")
        break
    else:
        print("invalid input")

