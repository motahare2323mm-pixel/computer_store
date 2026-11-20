
computer_shop = {
    "1": "show product",
    "2": "add product",
    "3": "remove product",
    "4": "search product",
    "5": "calculate total inventory product",
    "6":"count of the productse",
    "7": "exit"
}

products = {
    "cpu": 8500000,
    "ram": 2500000,
    "ssd": 4000000,
    "mouse": 800000
}
counts={
    "cpu": 5,
    "ram": 4,
    "ssd": 16,
    "mouse": 80
}


def total(products):
    total_price = 0
    for key in products:
        total_price = products[key]*counts[key] + total_price
    return total_price


while True:
    print("\n========== COMPUTER SHOP ==========")

    for key in computer_shop:
        print(key + " - " + computer_shop[key])

    choose = input("Choose a list number: ")

    if choose == "1":
        print("\n----- PRODUCT LIST -----")
        for item in products:
            print(item, "-", format(products[item], ","))

    elif choose == "2":
        name = input("Enter the name of the product to add: ").lower()
        
        if name in products:
            print("This product already exists!")
        else:
            price = input("Enter the price of the product: ")
            count=int(input("enter the count of products:"))
            
            if price.isdigit():
                products[name] = int(price)
                counts[name] = count
                print("Product added successfully!")
            else:
                print("Invalid price!")

    elif choose == "3":
        name = input("Enter the product name to remove: ").lower()

        if name in products:
            del products[name]
            del counts[name]
            print("Product removed successfully!")
        else:
            print("Product not found!")

    elif choose == "4":
        name = input("Enter the product name to search: ").lower()

        if name in products:
            print(name, "-", format(products[name], ","))
            print(name,"counts", "-", format(counts[name],","))
        else:
            print("Product not found!")

    elif choose == "5":
        result = total(products)
        print("Total inventory price:", format(result, ","))
    elif choose=="6":
        for key in counts:
         print(key+"-",+counts[key],"remained")
    elif choose == "7":
        print("Thank you for using Computer Shop!")
        break

    else:
        print("Invalid choice! Please try again.")
