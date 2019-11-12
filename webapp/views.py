from django.shortcuts import render

def index(request):
    """ The home page for webapp """

    return render(request, 'index.html')
