Shoppingcart={}
print("WELCOME TO THE AMANDO SHOPPING SITE \n1.Add a product to the cart \n2.Search for a product\n3.Delete a product from the cart\n4.Display the contents of the cart.\n5.Purchase items\n6.Quit ")
x = int(input("Enter Value: "))
i=1
while x!=6:
   
    if x==1:

        a=input(" What is the product-name and brand")
        b=float(input("product-price"))
        Shoppingcart.update({a:b})

    elif x==2:

        c=(input("What you want to search"))
        if c in Shoppingcart:
            print(c,"-",Shoppingcart[c])
        else:
            print("Not Found")         

    elif x==3:
         d=(input("What product do you want to delete"))
         if d in Shoppingcart:
             del Shoppingcart[d]
         else :
             print("Not found")   
    elif x==4:
         e=(input("Display the contents in the cart"))
         print(Shoppingcart)
    elif x==5:
          f=(input("What are the purchasing items"))
          print(Shoppingcart)
    print("WELCOME TO THE AMANDO SHOPPING SITE \n1.Add a product to the cart \n2.Search for a product\n3.Delete a product from the cart\n4.Display the contents of the cart.\n5.Purchase items\n6.Quit ")
    x = int(input("Enter Value: "))




   




    

       



        



