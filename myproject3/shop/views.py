from django.shortcuts import render #this will connect 

def product_list(request): #function created for the shop 
   return render(request, 'shop/product_list.html')
