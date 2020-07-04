from django.http import HttpResponse


def test(request):
    return HttpResponse("it's test views! ")