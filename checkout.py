#checkout program with listener while loop
def checkout():
    total = 0       #keeps track of the total
    count = 0       #keeps track of how many items were typed
    items = True    #the user did not write "done"
    while items:
        price = input('Enter price of item (Type "done" to exit): ')
        if price != 'done':                             #as long as the user does not type "done", the loops continues 
            count = count + 1
            total = float(total) + float(price)
            print("Subtotal: $ {:.2f}".format(total))   #this format only prints the first 2 decimals
        else:
            items = False                                #the user has typed "done"
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print("Average price per item: $ {:.2f}".format(average)) 

checkout()