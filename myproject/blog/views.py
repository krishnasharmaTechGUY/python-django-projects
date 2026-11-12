from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to the cool blog ")


def about(request):
    return HttpResponse("this is blog about page")
