
cnt = 'Y'
while cnt == 'Y' or cnt == 'y':
    buyPrice = float(input("Buy Price : "))
    sellPrice = float(input("Sell Price : "))
    qty = int(input("Qty : "))
    print("P/L : "+str((sellPrice-buyPrice)*float(qty)))
    cnt = input("Want to Continue?(Y/N) : ")

