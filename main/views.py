from django.shortcuts import render

# Create your views here.
def MainView(request):
    if request.method == 'GET':
        return render(request, 'main/main.html')