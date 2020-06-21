from django.shortcuts import render

# Create your views here.
def account_first_page(requset):
    return render(requset, 'account/account_first_page.html')
