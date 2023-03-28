def main():
    price = 50
    while(price>0):
        print("Amount Due:",price)
        given_coin = int(input("Insert Coin: "))
        if(given_coin == 5 or given_coin == 10 or given_coin ==25):
            price = price - given_coin
        if(price<=0):
            print("Change Owed:",-price)
main()
