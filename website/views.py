from django.http import HttpResponse


def index_view(request):
    return HttpResponse("<h1>This is the home page</h1>")


def about_view(request):
    return HttpResponse("<h1>This is the about page.</h1>")


def contact_view(request):
    return HttpResponse("<h1>This is the contact page</h1>")
