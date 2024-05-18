print("You are exploring a rainforest in search of treasure. Legend has it that there are some buried on a nearby island.")

question1=input("You come across a lake. Do you want to swim across, or wait for a boat? (swim/wait):")

if question1 == "swim":
    print("You get eaten by a hungry shark. Game over.") 
    exit()
else:
    if question1 == "wait":
        print("A boat arrives and you arrive at the island safely.")
        question2=input("You come to a cave. Do you want to venture inside or walk on? (venture/walk):")
        if question2 == "venture":
            print("Your are squished by boulders never to be seen again. Game over.")
            exit()
        else:
            if question2 == "walk":
                question3=input("Your at a crossroad. Do you go left, right, or straight? (left/right/straight): ")
                if question3=="left":
                    print("You are trampled by a herd of wildebeest. Game over.")
                    exit()
                elif question3=="straight":
                    print("You get stung by a poisonous wasp. Game over. ")
                    exit()
                elif question3=="right":
                    print("You march on and find the buried treasure! Yippee!!")
                    exit()
                
