Shoppingcart={}
print("WELCOME TO THE AMANDO SHOPPING SITE \n1.Add a product to the cart \n2.Search for a product\n3.Delete a product from the cart\n4.Display the contents of the cart.\n5.Purchase items\n6.Quit ")
x = int(input("Enter Value: "))
i=1
while x!=6:
   
    if x==1:
        if len(Shoppingcart)>=5:
                     print("The cart is full")
        else:
         a=input(" What is the product-name and brand ")
         b=float(input(" What is price of the product "))
         Shoppingcart.update({a:b})
        
  
        
    elif x==2:

        c=(input("What you want to search "))
        if c in Shoppingcart:
            print(c,"-",Shoppingcart[c])
            print(Shoppingcart)
        else:
            print("No Product Exists With This name")         

    elif x==3:
         d=(input("What product do you want to delete "))
         if d in Shoppingcart:
             del Shoppingcart[d]
             print("Delete Product Successfully")
         else :
             print("Product not found in cart")   
    elif x==4:
      print(Shoppingcart)
    elif x==5:
          g=input("Complete purchase(Y/N)")
          if g=="Y":
            print("Thank you for your business")
          else :
              print("Please Continue Shopping")
               
          print(Shoppingcart)
    
    
    print("WELCOME TO THE AMANDO SHOPPING SITE \n1.Add a product to the cart \n2.Search for a product\n3.Delete a product from the cart\n4.Display the contents of the cart.\n5.Purchase items\n6.Quit ")
    x = int(input("Enter Value: "))
   




   




    

       



        



