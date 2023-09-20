from django.shortcuts import render


def home(request):
    templates_name = "home.html"
    return render(request, templates_name)


def main(request):
    templates_name = "main.html"
    return render(request, templates_name)


def test(request):
    templates_name = "test.html"
    return render(request, templates_name)
