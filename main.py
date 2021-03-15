# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "nickle": .5,
    "penny": .1,
    "quarter": .25,
    "dime": .10
}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    running = True
    while running:
        command = input('what would you like?')
        if command == 'off':
            running = False
        elif command == 'report':
            for key in resources:
                print('%s: %s' % (key, resources[key]))
        elif command in ['latte', 'cappuccino', 'espresso']:
            ingredients = MENU[command]['ingredients']
            available = True
            for key in ingredients:
                if ingredients[key] > resources[key]:
                    print(f'{key} needs to be restocked')
                    available = False
                    break
            if available:
                cost = MENU[command]["cost"]
                amountPaid = 0
                while amountPaid < cost:
                    coin = input(f'{command} cost is {cost} please insert coins {cost - amountPaid} left to pay')
                    if coin in coins:
                        amountPaid += coins[coin]
                    else:
                        print('wrong change inserted please insert correct change')
                print(f"here is your {command}")
                for key in ingredients:
                    resources[key] -= ingredients[key]


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
