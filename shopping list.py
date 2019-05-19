#Shopping List

items=['apples', 'oranges', 'bananas']
#no_items= int(input('How may things do you want to add?'))

for i in range(10):
    items.append(input('What wlse would you like to add? \n (Hit enter when completed) '))
    print('Youre list so far ', items)
    moreitems = input('Anything else? ')
    items.append(moreitems)
    if moreitems == '':
        break
    else:
        continue

while '' in items:
    items.remove('')

print('Here is your shopping list: ', items)
