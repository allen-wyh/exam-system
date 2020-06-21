from django.shortcuts import render

# Create your views here.
def competion_first_page(request):
    return render(request, 'competition/competition_first_page.html')