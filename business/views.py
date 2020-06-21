from django.shortcuts import render

# Create your views here.
def business_first_page(request):
    return render(request, 'business/business_first_page.html')