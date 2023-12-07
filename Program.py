Shoppingcart={}
print("WELCOME TO THE AMANDO SHOPPING SITE \n1.Add a product to the cart \n2.Search for a product\n3.Delete a product from the cart\n4.Display the contents of the cart.\n5.Purchase items\n6.Quit ")
x = int(input("Enter Value: "))

a=input(" What is the product-name")
b=float(input("product-price"))
c=input(" What's brand is this")

i=1
while(i<=x):
    y=input("Enter Key")
    z=input("Enter value")
    Shoppingcart.update({y:z})
    i=i+1

   



        



