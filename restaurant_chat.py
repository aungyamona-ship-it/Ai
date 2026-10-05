def show_menu():
    print("\n--- MENU ---")
    print("Burger - $8")
    print("Pizza - $10")
    print("Fries - $4")
    print("Tacos - $7")
    print("Soda - $2")

def get_price(item):
    if item == "burger":
        return 8
    if item == "pizza":
        return 10
    if item == "fries":
        return 4
    if item == "tacos":
        return 7
    if item == "soda":
        return 2
    else:
        return 0

def take_order():
    order = []
    total = 0

    while True:
        print("What would you like to order? Type 'done' when finished: ")
        item = input().lower()

        if item == "done":
            break
        price = get_price(item)

        if price > 0:
            order.append(item)
            total += price
            print(item, "added to your order.")
        else:
            print("Sorry, that item is not on the menu.")

        return order, total

def main():
    print("Welcome to our restaurant!")

    name = input("What is your name? : ")
    print("Hello", name + "!")

    show_menu()

    order, total = take_order()

    print("\nYour order:")
    for item in order:
        print("-", item)

    print("Subtotal: $", total)

    print("Would you like delivery or pickup? ")
    choice = input().lower()

    if choice == "delivery":
        location = input("What is your location? : ")
        delivery_charge = 5
        total += delivery_charge
        print("Delivery to:", location)
        print("Delivery charge: $5")

    if total > 25:
        discount = total * 0.10
        total -= discount
        print("10 percent discount applied!")

    print("\nFinal price: $", round(total, 2))
    print("Would you like to place another order? ")
    again = input().lower()

    if again == "yes":
        main()
    else:
        print("Thank you for ordering,",name + "!")

main()