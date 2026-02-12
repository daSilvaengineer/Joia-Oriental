from django.shortcuts import render


def about_page(request):
    return render(request, "store/pages/about.html")
