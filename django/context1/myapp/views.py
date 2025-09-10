from django.shortcuts import render

# Create your views here.
i=0
def index(request):
    global i
    i += 1
    return render(request, 'index.html',{'num': i})
