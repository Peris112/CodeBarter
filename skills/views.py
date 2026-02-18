from django.shortcuts import render

# Create your views here.
def add(request):
    return render(request, 'skills/add_skill.html')
def myskills(request):
    return render(request, 'skills/myskills.html')
def details(request):
    return render(request, 'skills/skill_details.html')
def index(request):
    return render(request, 'skills/skill_index.html')
