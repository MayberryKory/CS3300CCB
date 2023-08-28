from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1> CCB </h1> \n <h3> Clydes Coding Buisness</h3>')