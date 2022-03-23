import studentdata
import order

print('========================================')
print('OFFICIAL RECEIPT')
print('Student Name:', studentdata.sd['Student_Name'].title())
print('ID Number:', studentdata.sd['ID'].title())
print('Year:', studentdata.sd['Year'].title())
print('Course & Section:', studentdata.sd['Course_Section'].title())
print('----------------------------------------')
print('Qnty   Price     Description')
for i in range(len(order.items)):
    print(order.items[i], order.cart_price[i], order.cart[i], sep='      ')
print('\n\nTotal: Php', str(round(order.spent, 2)))
print('Cash: Php', studentdata.sd['Wallet_Value'])
print('Change: Php', str(round(order.allowance, 2)))
print('\n      Thank You For Dining With Us!')
print('            Please Come Again')
print('========================================')
