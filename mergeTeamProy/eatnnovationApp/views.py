from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
#Habilitamos el uso de mensajes en Django 
from django.contrib import messages
#Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm


# Create your views here.
def home (request):
    return render(request, 'eatnnovationApp/home.html')

def menu (request):
    return render(request, 'eatnnovationApp/menu.html')

class Menu (ListView):
    model = Product 


class ProductList(ListView):
    model = Product 

class ProductCreate(SuccessMessageMixin, CreateView): 
    model = Product # Llamamos a la clase 'Product' que se encuentra en nuestro archivo 'models.py'
    form = Product # Definimos nuestro formulario con el nombre de la clase o modelo 'Product'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'products' de nuestra Base de Datos 
    success_message = 'Product Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o Product
    def get_success_url(self):        
        return reverse('productList') # revisar la pagina a la que se va a redireccionar User 
      
class ProductDetail(DetailView): 
    model = Product # Llamamos a la clase 'Product' que se encuentra en nuestro archivo 'models.py' 

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = Product # Llamamos a la clase 'Product' que se encuentra en nuestro archivo 'models.py' 
    form = Product # Definimos nuestro formulario con el nombre de la clase o modelo 'Product' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'products' de nuestra Base de Datos 
    success_message = 'Product Updated Succesfully !' # Mostramos este Mensaje luego de Editar un Product 

    # Redireccionamos a la página principal luego de actualizar un registro o Product
    def get_success_url(self):               
        return reverse('productList') # Redireccionamos a la vista principal 'leer'

class ProductDelete(SuccessMessageMixin, DeleteView): 
    model = Product 
    form = Product
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Product
    def get_success_url(self): 
        success_message = 'Product deleted Succesfully !' # Mostramos este Mensaje luego de Editar un Product 
        messages.success (self.request, (success_message))       
        return reverse('productList') # Redireccionamos a la vista principal 'leer'  
    

def registro(request):
    data = {
        'form' : CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(reverse('home'))
        data['form'] = formulario


    return render(request, 'registration/registro.html', data)