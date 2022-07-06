from django.shortcuts import render

# Create your views here.
# Add the import;  in order to use the HttpResponsefunction, we must import it like the others we've used so far.
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Cat:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]

# for raw text or an html string use HttpResponse
# for full template html file use render

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello World /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# Define the about view
def about(request):
    return render(request, 'about.html')

# Index view
def cats_index(request):
    return render(request, 'cats/index.html', { 'cats': cats })