from django.shortcuts import render

# Create your views here.


def homeView(request):
    return render(request, template_name="accounts/index.html")

def aboutSection(request):
    return render(request, template_name="accounts/about.html")