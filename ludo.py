import random
while(True):
    pp=input("type 'y' or 'n':")
    if pp=="n":
        print("Game has been finished!!!..")
        break   
    choice=[1,2,3,4,5,6,7,8,9,10,11,12]
    cd=random.choices(choice)
    ud=random.choices(choice)
    lis=["\u2680","\u2680","\u2681","\u2682","\u2683",'\u2684','\u2685','\u2687']
    print(lis[-1])
    for i in range(len(lis)):
        if i==cd[0]:
            emo=lis[i]
        elif i==ud[0]:
            emo2=lis[i]
        elif cd[0]>=len(lis):
            emo=lis[6]
        elif ud[0]>=len(lis):
            emo2=lis[6]
    print("computer dice",emo)
    print("computer score",cd)
    print("user dice",emo2)
    print("user score",ud)
    if cd[0]>10 and ud[0]<=10:
        print("computer wins")
    elif ud[0]>10 and cd[0]<=10:
        print('user wins')
    elif ud[0]>10 and cd[0]>10:
        print('tie')


