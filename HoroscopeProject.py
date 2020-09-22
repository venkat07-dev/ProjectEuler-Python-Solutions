#An horoscope program to know the daily horoscope based on your zodiac sign....

start=True
while start == True:
    print("\nChoose Your Zodiac Sign and I will let you know your Horoscope")
    print('''
    1.Aries
    2.Taurus
    3.Gemini
    4.Cancer
    5.Leo
    6.Virgo
    7.Libra
    8.Scorpio
    9.Sagittarius
    10.Capricorn
    11.Aquarius
    12.Pisces
''')
#Take the input
    i = int(input("Enter your zodiac number corresponding to your Zodiac Sign to get started : "))

#Corresponding output generated based on input matched
    if i == 1:
        print('''\nARIES!!!\nProfession:\nYou are climbing up the ladder of your career.Keep on climbing and keep on pushing yourself even when it gets hard. 
The reward is going to be worth it and you will be proud of yourself.
\nLuck:\nThe numbers 19 and 2 are going to be your lucky numbers today.
\nTravel:\nToday isn't the best day for you to travel. Try to postpone whatever plans you might have. Traveling is in your near future, however.''')
    elif i == 2:
        print('''\nTAURUS!!!\nProfession:\nYour boss and your co-workers love how energetic and optimistic you are and how you can lift anyone's spirit.A Scorpio will irritate you at work, but don't let it get to your head.\n
Luck:\nBeing around a very happy Leo is going to bring you lots of luck today. Buy a lottery ticket!\n
Travel:\nWhen traveling, remember to be frugal, not cheap. Enjoy yourself, but don't overspend.''')
    elif i == 3:
        print('''\nGEMINI!!!\nProfession:\nThere is something that is nagging you.It's related to your finances and it's been on your mind constantly. 
A Cancer co-worker will keep you entertained at work today.\n
Luck:\nThe number 54 is going to be your lucky number today. You will have good luck when buying a vehicle today.\n
Travel:\nIf you haven't done it, it would be great if you travelled with your best friend this year. Be ready to laugh a lot together!''')
    elif i == 4:
        print('''\nCANCER!!!\nProfession:\nYou are not so sure anymore when it comes to your career.You might even start thinking about changing career paths.
Start looking around for other options.\n
Luck:\nYou, sadly, won't have lots of good luck today. Minor luck will follow you in social interactions but don't expect any financial luck.\n
Travel:\nEven though today isn't the best day for you to travel, it's a great day to start planning an adventurous trip.''')
    elif i == 5:
        print('''\nLEO!!!\nProfession:\nBy nature, you are a diligent worker, and now you can see how good it feels to see that all your hard work really is worth it. 
Financially, you are going through a rough patch right now.\n
Luck:\nYour lucky numbers will be every number that has the number 7 in it. Don't invest in the stock market.\n
Travel:\nWhen traveling, always make sure that you buy travel insurance. Better to be safe than sorry.''')
    elif i == 6:
        print('''\nVIRGO!!!\nProfession:\nSpend some time with your co-workers, especially if someone wants to give you advice or if you have any advice for a younger colleague. 
Unemployed signs will get a life changing opportunity today.\n
Luck:\nupiter, the planet that governs good fortune, is sending some powerful energy your way today. 
Be on the lookout for the number 22.\n
Travel:\nIf you are traveling today, or someday soon, make sure that you make a list of all the things that you need to bring with you.
Don't over pack.''')
    elif i == 7:
        print('''\nLIBRA!!!\nProfession:\nDon't borrow money from people and don't invest or buy anything big, especially on a loan. Focus on earning and setting money aside. 
You will really need it later on in the month.\n
Luck:\nYou will have some minor luck when it comes to your financial situation today. The color blue will bring you some luck.\n
Travel:\nTry some of the local food. When traveling, make sure that you are experiencing a different culture. 
Remember to be respectful.''')
    elif i == 8:
        print('''\nSCORPIO!!!\nProfession:\nYou like being independent and you try to be independent as much as you can. You feel focused, good and ready to take on any action.
Financially, you could be doing better.\n
Luck:\nThe number 96 is going to bring you luck today. Don't gamble with a large sum of money, because you won't win.\n
Travel:\nIf you are thinking about traveling anytime soon, book a flight at least 2 or 3 months in advance to save on some money.''')
    elif i == 9:
        print('''\nSAGITTARIUS!!!\nProfession:\nHard work has been paying off, and you can finally feel it. An opportunity will show itself to you today.
Are you going to say yes to it or are you going to let it pass by?\n
Luck:\nThe numbers 1 and 16 are going to be your lucky numbers today. You will have luck if you are investing in real estate.\n
Travel:\nIf you are traveling with someone, be ready for the fact that you are going to have to make a lot of compromised while traveling.''')
    elif i == 10:
        print('''\nCAPRICORN!!!\nProfession:\nVenus, the planet that governs love and money, has your back today. Expect some income at the end of the day. 
Unemployed signs will receive a very interesting email today.\n
Luck:\nThe number 18 will bring you good luck and it will have a special meaning for you today.\n
Travel:\nToday isn't the best day for traveling. Be careful in traffic, especially if you are driving for a long time.''')
    elif i == 11:
        print('''\nAQUARIUS!!!\nProfession:\nSome people might owe you some money, but they will pay you back soon, so don't worry about that.
However, your career is at a standstill. Do something about that.\n
Luck:\nThe color orange is going to bring you good luck today.\n
Travel:\nTraveling with a family member will make the bond that the two of you have stronger and better.''')
    elif i == 12:
        print('''\nPISCES!!!\nProfession:\nFinancially, you are already doing a lot better. Learn to make a budget and stick to it. 
Try saving up some money for emergency situations.\n
Luck:\nToday not the best day to gamble with large sums of money. The number 9 is your lucky number of the day.\n
Travel:\nSome people like to travel alone and some people like to travel with their friends. However, you are thinking about traveling with complete strangers.''')
    else:
        print("Are you sure of your zodiac sign????")
        print("Try Again!!!!")
#To continue or exit from the program     
    start=True if input("\nDo you want to continue?(Yes/No):")=='Yes' else False
    if start==False:
        print("\nTHANK YOU, HAVE A NICE DAY")
