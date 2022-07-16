from django.shortcuts import render, redirect
# from django.http import HttpResponse
from main_app.forms import FeedingForm
from .models import Cat, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Cat, Toy, Photo
from .forms import FeedingForm

S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'catcollector-cw'


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
  # Get the toys the cat doesn't have
  toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  # render template, pass it the cat
  return render(request, 'cats/detail.html', { 
    'cat': cat,
    'feeding_form': feeding_form,
    'toys': toys_cat_doesnt_have
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

def add_photo(request, cat_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension also
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, cat_id=cat_id)
      photo.save()
    except:
      print('An error occurred')
  return redirect('detail', cat_id=cat_id)

def assoc_toy(request, cat_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Cat.objects.get(id=cat_id).toys.add(toy_id)
  return redirect('detail', cat_id=cat_id)

def delete_toy(request, cat_id, toy_id):
  Cat.objects.get(id=cat_id).toys.remove(toy_id)
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