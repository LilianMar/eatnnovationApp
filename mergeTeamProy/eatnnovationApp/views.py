from django.shortcuts import render, redirect
# Import de nuestros modelos
from .models import Product , Invoice , Category
#Import de nuestras vistas
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
from django.contrib.auth import get_user_model
#Habilitamos el uso de mensajes en Django 
from django.contrib import messages
#Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

# Autenticación de usuario Staff
def is_staff(user):
    return user.is_authenticated and user.is_staff

# Vista para el home
def home (request):
    return render(request, 'eatnnovationApp/home.html')

# Vista para el menú
def menu (request):
    return render(request, 'eatnnovationApp/menu.html')

# Vistas para el modelo Productos

class Menu (ListView):
    model = Product 

# Uso de decoradores para la autenticación en productos
@method_decorator(user_passes_test(is_staff), name='dispatch')
class ProductList(ListView):
    model = Product 

@method_decorator(user_passes_test(is_staff), name='dispatch')
class ProductCreate(SuccessMessageMixin, CreateView): 
    model = Product # Llamamos a la clase 'Product' que se encuentra en nuestro archivo 'models.py'
    form = Product # Definimos nuestro formulario con el nombre de la clase o modelo 'Product'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'products' de nuestra Base de Datos 
    success_message = 'Product Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o Product
    def get_success_url(self):        
        return reverse('productList') # revisar la pagina a la que se va a redireccionar User 

@method_decorator(user_passes_test(is_staff), name='dispatch')      
class ProductDetail(DetailView): 
    model = Product # Llamamos a la clase 'Product' que se encuentra en nuestro archivo 'models.py' 

@method_decorator(user_passes_test(is_staff), name='dispatch')
class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = Product # Llamamos a la clase 'Product' que se encuentra en nuestro archivo 'models.py' 
    form = Product # Definimos nuestro formulario con el nombre de la clase o modelo 'Product' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'products' de nuestra Base de Datos 
    success_message = 'Product Updated Succesfully !' # Mostramos este Mensaje luego de Editar un Product 

    # Redireccionamos a la página principal luego de actualizar un registro o Product
    def get_success_url(self):               
        return reverse('productList') # Redireccionamos a la vista principal 'leer'

@method_decorator(user_passes_test(is_staff), name='dispatch')
class ProductDelete(SuccessMessageMixin, DeleteView): 
    model = Product 
    form = Product
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Product
    def get_success_url(self): 
        success_message = 'Product deleted Succesfully !' # Mostramos este Mensaje luego de Editar un Product 
        messages.success (self.request, (success_message))       
        return reverse('productList') # Redireccionamos a la vista principal 'leer'   

# Vistas para el modelo Usuarios   

User = get_user_model()

# Uso de decoradores para la autenticación en usuarios
@method_decorator(user_passes_test(is_staff), name='dispatch')
class UserList(ListView):
    model = User 

@method_decorator(user_passes_test(is_staff), name='dispatch')
class UserCreate(SuccessMessageMixin, CreateView): 
    model = User # Llamamos a la clase User que se encuentra en nuestro archivo 'models.py'
    form = User # Definimos nuestro formulario con el nombre de la clase o modelo User
    fields = ['username', 'email','is_superuser', 'is_staff', 'password'] # Le decimos a Django que muestre todos los campos de la tabla users de nuestra Base de Datos 
    success_message = 'User Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o User
    def get_success_url(self):        
        return reverse('userList') 
      
@method_decorator(user_passes_test(is_staff), name='dispatch')
class UserDetail(DetailView): 
    model = User # Llamamos a la clase User que se encuentra en nuestro archivo 'models.py' 

@method_decorator(user_passes_test(is_staff), name='dispatch')
class UserUpdate(SuccessMessageMixin, UpdateView): 
    model = User # Llamamos a la clase User que se encuentra en nuestro archivo 'models.py' 
    form = User # Definimos nuestro formulario con el nombre de la clase o modelo User 
    fields = ['username', 'email','is_superuser', 'is_staff', 'password'] # Le decimos a Django que muestre todos los campos de la tabla users de nuestra Base de Datos 
    success_message = 'User Updated Succesfully !' # Mostramos este Mensaje luego de Editar un User 

    # Redireccionamos a la página principal luego de actualizar un registro o User
    def get_success_url(self):               
        return reverse('userList') # Redireccionamos a la vista principal 'leer'

@method_decorator(user_passes_test(is_staff), name='dispatch')
class UserDelete(SuccessMessageMixin, DeleteView): 
    model = User 
    form = User
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o User
    def get_success_url(self): 
        success_message = 'User deleted Succesfully !' # Mostramos este Mensaje luego de Editar un User 
        messages.success (self.request, (success_message))       
        return reverse('userList') # Redireccionamos a la vista principal 'leer'  
    
# Para hacer el registro con ayuda de Django admin y se sube en la base de datos
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

# Para que se guarde la cantidad de productos que se van seleccionando en el Order Now
def select_products(request):
    if request.method == 'POST':
        selected_products = []
        total_quantity = int(request.POST.get('total_quantity', 0))
        
        for i in range(1, total_quantity + 1):
            product_id = request.POST.get(f'product_id_{i}')
            quantity = int(request.POST.get(f'quantity_{i}', 0))
            
            if product_id and quantity > 0:
                product = Product.objects.get(id=product_id)
                selected_products.append({'product': product, 'quantity': quantity})
        
        context = {
            'selected_products': selected_products,
            'user': request.user,
        }
        return render(request, 'eatnnovationApp/order_confirmation.html', context)
    else:
        products = Product.objects.all()
        context = {'object_list': products}
        return render(request, 'eatnnovationApp/orders.html', context)

# Se guarda la información de la factura en la base de datos
def order_confirmation(request):
    if request.method == 'POST':
        selected_products = []
        total_amount = 0

        for i, (product_id, quantity) in enumerate(request.POST.items()):
            if product_id.startswith('quantity_') and quantity.isdigit():
                product_id = product_id.split('_')[1]
                product = Product.objects.get(id=product_id)
                quantity = int(quantity)
                subtotal = product.price * quantity
                total_amount += subtotal
                selected_products.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})

                product.availableCant -= quantity
                product.save()

        user = request.user
        invoice = Invoice(user=user, total_amount=total_amount)
        invoice.save()

        context = {
            'products': selected_products,
            'total_amount': total_amount,
        }
        return render(request, 'eatnnovationApp/order_confirmation.html', context)
    else:
        return redirect('select_products')
    
#Vistas para el modelo Categorías

# Uso de decoradores para la autenticación en categorías
@method_decorator(user_passes_test(is_staff), name='dispatch')
class CategoryList(ListView):
    model = Category 

@method_decorator(user_passes_test(is_staff), name='dispatch')
class CategoryCreate(SuccessMessageMixin, CreateView): 
    model = Category # Llamamos a la clase User que se encuentra en nuestro archivo 'models.py'
    form = Category # Definimos nuestro formulario con el nombre de la clase o modelo User
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla users de nuestra Base de Datos 
    success_message = 'Category Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o User
    def get_success_url(self):        
        return reverse('categoryList')
    
@method_decorator(user_passes_test(is_staff), name='dispatch')
class CategoryUpdate(SuccessMessageMixin, UpdateView): 
    model = Category # Llamamos a la clase 'Product' que se encuentra en nuestro archivo 'models.py' 
    form = Category # Definimos nuestro formulario con el nombre de la clase o modelo 'Product' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'products' de nuestra Base de Datos 
    success_message = 'Category Updated Succesfully !' # Mostramos este Mensaje luego de Editar un Product 

    # Redireccionamos a la página principal luego de actualizar un registro o Product
    def get_success_url(self):               
        return reverse('categoryList') # Redireccionamos a la vista principal 'leer'

@method_decorator(user_passes_test(is_staff), name='dispatch')
class CategoryDelete(SuccessMessageMixin, DeleteView): 
    model = Category 
    form = Category
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Product
    def get_success_url(self): 
        success_message = 'Category deleted Succesfully !' # Mostramos este Mensaje luego de Editar un Product 
        messages.success (self.request, (success_message))       
        return reverse('categoryList') # Redireccionamos a la vista principal 'leer'      
    
@method_decorator(user_passes_test(is_staff), name='dispatch')
class InvoiceList(ListView):
    model = Invoice
