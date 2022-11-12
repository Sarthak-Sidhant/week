#create a program to calculate the lemons given to you by life
#and the money you can make from it
#thinking of more collaborative ideas with lemon
print("Welcome to the lemon theory!")
print("this program will help you calculate what you can do with the lemons you've been given by life")
quant=int(input("How many lemons have you been given? "))

valid_size=False
while valid_size == False:   
    size=round(float(input("How big are the lemons? (radius in inches): ")),1)
    if size <= 0:
        print("Invalid size")
    elif size > 30:
        print("nah bro i never saw that big of a lemon u def kidding me :/")
    else:
        valid_size=True

valid_color=False
while valid_color == False:
    ll=input("what color is the lemon? yellow/green: ")
    if ll == "yellow":
        lemon_type = 2
        valid_color=True
    elif ll == "green":
        lemon_type = 1.5
        valid_color=True
    else:
        print("thats some weird color for a lemon")
        valid_color=False

print("thats cool and all, our lemon-experts with lemonalyze your lemons and give you a lemon score")
print("we will also recommend you the ways with which you can utilise your lemons")
lemon_score = quant + (size ** lemon_type)
print("your lemon score is", lemon_score)
print("now we'll recommend you the ways you can use your lemons")
if quant < 10 or lemon_type == 1.5 or size < 0.5:
    print("sorry, but you can't use your lemons to make lemonades")
    print("this is because you don't have enough lemons or your lemons are too small or green")
    print("please dont feel bad, you can still sell your lemons to the lemonade stand")
    if lemon_type == 1.5 and size >= 0.5 and size < 1:
        price = quant * 5
        print("you can sell your lemons for Rs 5 each")
    elif lemon_type == 1.5 and size >= 1 and size < 2:
        price = quant * 10
        print("you can sell your lemons for Rs 10 each")
    elif lemon_type == 1.5 and size >= 2 and size < 3:
        price = quant * 15
        print("you can sell your lemons for Rs 15 each")
    elif lemon_type == 1.5 and size >= 3 and size < 4:
        price = quant * 20
        print("you can sell your lemons for Rs 20 each")
    elif lemon_type== 2 and size > 0.5 and size < 1.5:
        price = quant * 15
        print("you can sell your lemons for Rs 15 each")
    elif lemon_type == 2 and size > 1.5 and size < 2:
        price = quant * 25
        print("you can sell your lemons for Rs 25 each")
    elif lemon_type == 2 and size > 2 and size < 3:
        price = quant * 35
        print("you can sell your lemons for Rs 35 each")
    print("you can make", price , "coins from your lemons")
    print("thank you for using lemon theory")
    print("we were happy to help you!")
    print("please come again!")
    print("goodbye!")
elif quant > 10 and lemon_type == 2 and size > 0.5:
    print("you can make lemonades with your lemons")
    print("you can also sell your lemons alternative")
    lorl=input("do you want to make lemonades or sell your lemons? lemonade/sell: ")
    if lorl == "lemonade":
        sqz=int(input("how many lemons can you squeeze in a day: "))
        if sqz > 10:
            print("with that many lemons you can make a lot of lemonades")
            print("you can make 1 lemonade for 1 Lemon each")
            print("you can make", quant, "lemonades")
            print("one lemonade sells for Rs 50")
            print("you can make", quant * 50, "coins")
            print("thank you for using lemon theory")
            print("we were happy to help you!")
            print("please come again!")
            print("goodbye!")
        elif sqz < 10:
            print("you cant make lemonades with that less of an effort, you need to squeeze more lemons")
            print("you can sell your lemons instead")
            print("you can sell your lemons for Rs 15 each")
            print("you can make", quant * 15, "coins")
            print("thank you for using lemon theory")
            print("we were happy to help you!")
            print("please come again!")
            print("goodbye!")
    elif lorl == "sell":
        if lemon_type== 2 and size > 0.5 and size < 1.5:
            price = quant * 15
            print("you can sell your lemons for Rs 15 each")
        elif lemon_type == 2 and size > 1.5 and size < 2:
            price = quant * 25
            print("you can sell your lemons for Rs 25 each")
        elif lemon_type == 2 and size > 2 and size < 3:
            price = quant * 35
            print("you can sell your lemons for Rs 35 each")
        print("you can make", price , "coins from your lemons")
        print("thank you for using lemon theory")
        print("we were happy to help you!")
        print("please come again!")
        print("goodbye!")
    else:
        print("invalid input")
        print("please try again")
        print("thank you for using lemon theory")
        print("run the program again to use lemon theory")
        print("goodbye!")
else:
    print("invalid input")
    print("please try again")
    print("run the program again to use lemon theory")
    print("goodbye!")
