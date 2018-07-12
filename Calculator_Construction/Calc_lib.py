import webbrowser as wb


def cementtoall():

    cement = int(input("\nInput your kg of cement: "))
    aggregate = 3  # aggregate(stones)
    sand = 3
    aggregatetot = aggregate * cement
    sandtotal = sand * cement
    print("For %s cement you will need %s stones and %s sand! \n \n" % (cement, aggregatetot, sandtotal))


def sandtoall():
    sand = int(input("\nInput your kg of sand: "))
    cementtot = int(sand / 3)
    aggregatetot = int(sand)
    print("For %d sand, you will need %d aggregate(stones) and %d cement! \n \n" % (sand, aggregatetot, cementtot))


def aggregatetoall():
    aggregate = int(input("\nEnter your aggregate(stones) kg: "))
    cementtot = int(aggregate / 3)
    sandtot = int(aggregate)
    print("For %d kg aggregate, you will need %d kg sand and %d kg cement! \n \n" % (aggregate, sandtot, cementtot))


def recommend():
    print("\nWe can recommend you some nice sand, stones and cement to buy and use!")
    print("Ok! We'll open your default browser to recommend you!")
    wb.open('https://www.kaxirismonotika.gr/τσιμεντα/518-tsimento-.html', new=2)
    print("Have a nice day! We hope, we helped you find the right mixture for your concrete! \n \n")
