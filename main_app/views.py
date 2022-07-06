from django.shortcuts import render

# Create your views here.
# Add the import;  in order to use the HttpResponsefunction, we must import it like the others we've used so far.
from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello World /ᐠ｡‸｡ᐟ\ﾉ</h1>')
