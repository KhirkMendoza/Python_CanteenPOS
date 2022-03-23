available = [4, 4, 2, 2, 1, 5, 5, 3, 5, 4]
details = [
    'Soda', 'Bottled Water', 'Coffee', 'Tea',
    'Bread', 'Apple', 'Banana', 'Oranges',
    'Tapsilog', 'Porksilog']
price = [29.25, 20.00, 50.00, 35.50, 15.00,
         20.50, 15.00, 25.10, 80.99, 80.99]

print('--------------------------------------------')
print('\n             Welcome!')
print('     Here is Our Menu For Today.')
print('\nOption' + '  Available' + '   Details' + '       Price')
print(' [1]' + '        ' + str(available[0]) + '       ' + details[0] + '            ' + str(price[0]))
print(' [2]' + '        ' + str(available[1]) + '       ' + details[1] + '   ' + str(price[1]))
print(' [3]' + '        ' + str(available[2]) + '       ' + details[2] + '          ' + str(price[2]))
print(' [4]' + '        ' + str(available[3]) + '       ' + details[3] + '             ' + str(price[3]))
print(' [5]' + '        ' + str(available[4]) + '       ' + details[4] + '           ' + str(price[4]))
print(' [6]' + '        ' + str(available[5]) + '       ' + details[5] + '           ' + str(price[5]))
print(' [7]' + '        ' + str(available[6]) + '       ' + details[6] + '          ' + str(price[6]))
print(' [8]' + '        ' + str(available[7]) + '       ' + details[7] + '         ' + str(price[7]))
print(' [9]' + '        ' + str(available[8]) + '       ' + details[8] + '        ' + str(price[8]))
print(' [10]' + '       ' + str(available[9]) + '       ' + details[9] + '       ' + str(price[9]))
print('--------------------------------------------')
print(' [11]' + '       ' + 'Finish')
print(' [0]' + '        ' + 'Exit')

cart = []
items = []
cart_price = []
allowance = 150.0
spent = 0


def order():

    global allowance
    global spent

    if allowance < 0:
        print('\nInsufficient Balance!')
        print('Please Try Again Later')
        quit()
    else:
        print('\nTotal: Php ' + str(round(spent, 2)))
        print('You Only Have Php ' + str(round(allowance, 2)) + ' To Spend')
        while True:
            option = input('Enter Your Option: ')
            if option == '1':
                item = int(input('How many ' + details[0] + '?: '))
                if item > available[0]:
                    print('Sorry, ' + str(available[0]) + ' ' + details[0] + ' Left.')
                else:
                    available[0] = available[0] - item
                    cart_price.append(price[0] * item)
                    cart.append(details[0])
                    items.append(item)
                    spent = spent + (item * price[0])
                    allowance = allowance - (item * price[0])
                    order()
                    break
            elif option == '2':
                item = int(input('How many ' + details[1] + '?: '))
                if item > available[1]:
                    print('Sorry, ' + str(available[1]) + ' ' + details[1] + ' Left.')
                else:
                    available[1] = available[1] - item
                    cart_price.append(price[1] * item)
                    cart.append(details[1])
                    items.append(item)
                    spent = spent + (item * price[1])
                    allowance = allowance - (item * price[1])
                    order()
                    break
            elif option == '3':
                item = int(input('How many ' + details[2] + '?: '))
                if item > available[2]:
                    print('Sorry, ' + str(available[2]) + ' ' + details[2] + ' Left.')
                else:
                    available[2] = available[2] - item
                    cart_price.append(price[2] * item)
                    cart.append(details[2])
                    items.append(item)
                    spent = spent + (item * price[2])
                    allowance = allowance - (item * price[2])
                    order()
                    break
            elif option == '4':
                item = int(input('How many ' + details[3] + '?: '))
                if item > available[3]:
                    print('Sorry, ' + str(available[3]) + ' ' + details[3] + ' Left.')
                else:
                    available[3] = available[3] - item
                    cart_price.append(price[3] * item)
                    cart.append(details[3])
                    items.append(item)
                    spent = spent + (item * price[3])
                    allowance = allowance - (item * price[3])
                    order()
                    break
            elif option == '5':
                item = int(input('How many ' + details[4] + '?: '))
                if item > available[4]:
                    print('Sorry, ' + str(available[4]) + ' ' + details[4] + ' Left.')
                else:
                    available[4] = available[4] - item
                    cart_price.append(price[4] * item)
                    cart.append(details[4])
                    items.append(item)
                    spent = spent + (item * price[4])
                    allowance = allowance - (item * price[4])
                    order()
                    break
            elif option == '6':
                item = int(input('How many ' + details[5] + '?: '))
                if item > available[5]:
                    print('Sorry, ' + str(available[5]) + ' ' + details[5] + ' Left.')
                else:
                    available[5] = available[5] - item
                    cart_price.append(price[5] * item)
                    cart.append(details[5])
                    items.append(item)
                    spent = spent + (item * price[5])
                    allowance = allowance - (item * price[5])
                    order()
                    break
            elif option == '7':
                item = int(input('How many ' + details[6] + '?: '))
                if item > available[6]:
                    print('Sorry, ' + str(available[6]) + ' ' + details[6] + ' Left.')
                else:
                    available[6] = available[6] - item
                    cart_price.append(price[6] * item)
                    cart.append(details[6])
                    items.append(item)
                    spent = spent + (item * price[6])
                    allowance = allowance - (item * price[6])
                    order()
                    break
            elif option == '8':
                item = int(input('How many ' + details[7] + '?: '))
                if item > available[7]:
                    print('Sorry, ' + str(available[7]) + ' ' + details[7] + ' Left.')
                else:
                    available[7] = available[7] - item
                    cart_price.append(price[7] * item)
                    cart.append(details[7])
                    items.append(item)
                    spent = spent + (item * price[7])
                    allowance = allowance - (item * price[7])
                    order()
                    break
            elif option == '9':
                item = int(input('How many ' + details[8] + '?: '))
                if item > available[8]:
                    print('Sorry, ' + str(available[8]) + ' ' + details[8] + ' Left.')
                else:
                    available[8] = available[8] - item
                    cart_price.append(price[8] * item)
                    cart.append(details[8])
                    items.append(item)
                    spent = spent + (item * price[8])
                    allowance = allowance - (item * price[8])
                    order()
                    break
            elif option == '10':
                item = int(input('How many ' + details[9] + '?: '))
                if item > available[9]:
                    print('Sorry, ' + str(available[9]) + ' ' + details[9] + ' Left.')
                else:
                    available[9] = available[9] - item
                    cart_price.append(price[9] * item)
                    cart.append(details[9])
                    items.append(item)
                    spent = spent + (item * price[9])
                    allowance = allowance - (item * price[9])
                    order()
                    break
            elif option == '11':
                print('\n\nHere Is Your Receipt!\n\n')
                break
            elif option == '0':
                print('\n\nThank You, Come Again!')
                quit()
            else:
                print('\nInvalid Option!')
                return order()


order()
