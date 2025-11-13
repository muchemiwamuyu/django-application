from django.shortcuts import render

# Create your views here.
def hello_world(request):
    context = {'message': "Hello from the blogs platform!"}
    return render(request, 'index.html', context )
