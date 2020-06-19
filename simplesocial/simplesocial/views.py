from django.shortcuts import render


def TestPage(request):
    return render(request, 'test.html')

def ThanksPage(request):
    return render(request, 'thanks.html')

def HomePage(request):
    return render(request, 'index.html')