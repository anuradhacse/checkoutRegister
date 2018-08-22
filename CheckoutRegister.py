from product import Product

bar_code = 0
balance = 0
shopping_cart = []

def get_available_products():
    milk = Product("Milk", "2 Liters", 2, 123);
    bread = Product("Bread", "1 loaf", 8, 456);
    apple = Product("Apple", "1", 7, 654);
    suger = Product("Suger", "1 Kg", 12, 236);
    tomatoes = Product("Tomatoes", "0.5Kg", 6, 987);

    available_products = [];
    available_products.append(milk)
    available_products.append(bread)
    available_products.append(apple)
    available_products.append(suger)
    available_products.append(tomatoes)

    return available_products

def print_available_products(available_products):
    for product in available_products:
        print product.get_name()

def check_the_product_from_barcode(barcode):
    for product in available_products:
        if str(product.barcode) == bar_code:
            return product

    print "This product does not exist in our inventory."

def calculate_total(shopping_cart):
    total = 0;
    for product in shopping_cart:
        total += product.price
    return total

def print_final_receipt(shopping_cart, total_cost, paid_amount, balance):
    for product in shopping_cart:
        print product.name + " - " + product.weight + "            $" + str(product.price)

    print "Total amount due : $" + str(total_cost)
    print "Amount Received : $" + str(paid_amount)
    print "Change given : $" + str(balance)


def start_programme():
    print "----- Welcome to FedUni checkout! -----"
    while True:
        global bar_code, shopping_cart
        bar_code = raw_input("Please enter the barcode of your item: ")
        product = check_the_product_from_barcode(bar_code)

        if not (product is None):
            print product.name + " " + product.weight + " - $" + str(product.price)
            shopping_cart.append(product)

        proceed = raw_input("Would you like to scan another product? (Y/N)")

        if proceed == "N" or proceed == "n" or proceed == "No" :
            total = calculate_total(shopping_cart)
            print "Payment due: $" + str(total)
            amount_payed = 0
            balance = 0
            while amount_payed != total:
                amount = input("Please enter an amount to pay: ")
                if amount < 0:
                    print "We don't accept negative money!"
                elif amount < total:
                    amount_payed += amount
                    #cumulative  amount greater than total (ex: total 8$ / pay 3$ 3$ 3$ / balance 1$)
                    if amount_payed >= total:
                        balance = amount_payed - total
                        break
                #user input an amount greater than total(ex: total 8$ / pay 3$ and 10$ / balance 5$)
                else:
                    amount_payed += amount
                    balance = amount_payed - total
                    break

            print_final_receipt(shopping_cart, total, amount_payed, balance)

            print "Thank you for shopping at FedUni!"
            next_customer = raw_input("(N)ext customer, or (Q)uit? ")
            if next_customer == "q" or next_customer == "quit":
                break

            #empty the shopping cart
            shopping_cart = []



available_products = get_available_products()
print "There are " + str(len(available_products)) + " Products available in the Store!!! \n"
print print_available_products(available_products)

start_programme()


