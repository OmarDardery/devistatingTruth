from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "lie.html")
def truth(request):
    return render(request, "truth.html")
