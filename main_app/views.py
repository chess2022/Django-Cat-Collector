from django.shortcuts import render, redirect
# Add the import;  in order to use the HttpResponsefunction, we must import it like the others we've used so far.
# from django.http import HttpResponse
from main_app.forms import FeedingForm
from .models import Cat, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


# Add the Cat class & list and view function below the imports
# This is only necessary without an external database!!!
# class Cat:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cats = [
#   Cat('Lolo', 'tabby', 'foul little demon', 3),
#   Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]

# for raw text or an html string use HttpResponse
# for full template html file use render


# Create your views here.

# Define the home view
def home(request):
    # return HttpResponse('<h1>Hello World /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    return render(request, 'home.html')

# Define the about view
def about(request):
    return render(request, 'about.html')

# Index view
def cats_index(request):
    cats = Cat.objects.order_by('id')
    return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request, cat_id):
  # get the individual cat
  cat = Cat.objects.get(id=cat_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  # render template, pass it the cat
  return render(request, 'cats/detail.html', { 
    'cat': cat,
    'feeding_form': feeding_form
    })

def add_feeding(request, cat_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save to db until it has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

#Class-based Views are classes defined in the Django framework that we can extend and use instead of view functions.

class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats/'

class CatUpdate(UpdateView):
  model = Cat
  # disallow the renaming of a cat
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'