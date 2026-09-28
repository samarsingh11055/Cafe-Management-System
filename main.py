# Define the menu of restaurant
menu = {
    'Sandwich':80,
    'Red sauce pasta':85,
    'White sauce pasta':100,
    'Veg Burger':80,
    'Farmhouse pizza':130,
    'Garlic Bread':95,
    'Paneer buteer masala':180,
    'Paneer lababdar':195,
    'Kadhai Paneer':150,
    'Shahi Paneer':160,
    'Chicken butter masala':210

      
}

# Greet
print("WElcome to VISHWANATH Cafe")
print("Here is the menu for the day")
print("Sandwich: Rs80\nRed sauce pasta: Rs85\nWhite sauce pasta: Rs100\nVeg burger: Rs80\nFarmhouse pizza: Rs130\nGarlic Bread: Rs95\nPaneer buteer masala: Rs180\nPaneer lababdar: Rs195\nKadhai Paneer: Rs150\nShahi Paneer: Rs160\nChicken butter masala: Rs210")

order_total = 0
#80 + 70 = 150

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} is has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")
print("Thank You")
print("Please visit again")
    