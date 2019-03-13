from django.shortcuts import render

# Create your views here.
def res_request(request):
    return render(request, 'index.html')