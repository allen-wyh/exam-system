from django.shortcuts import render


def get_first_page(request):
    return render(request, 'exam_system.html')