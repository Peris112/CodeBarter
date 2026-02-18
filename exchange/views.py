from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'exchange/create_exch.html')
def details(request):
    return render(request, 'exchange/exch_details.html')
def index(request):
    return render(request, 'exchange/exch_index.html')
def my_exch(request):
    return render(request, 'exchange/my_exch.html')
