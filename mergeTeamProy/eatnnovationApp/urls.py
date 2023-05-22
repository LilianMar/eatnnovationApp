from django.urls import path
from .views import home,Menu
from  eatnnovationApp.views import ProductCreate,ProductDelete,ProductDetail,ProductList,ProductUpdate

urlpatterns = [
    path('', home, name="home"),
    
    path('menu/', Menu.as_view(template_name = "eatnnovationApp/menu.html"), name='menu'),
    # La ruta 'leer' en donde listamos todos los registros o Products de la Base de Datos
    path('productList/', ProductList.as_view(), name='productList'),
    # La ruta 'details' en donde mostraremos una página con los details de un Products o registro 
    path('productList/detail/<int:pk>', ProductDetail.as_view(template_name = "eatnnovationApp/detail_product.html"), name='detailProduct'),
    # La ruta 'create' en donde mostraremos un formulario para create un nuevo Products o registro  
    path('productList/create', ProductCreate.as_view(template_name = "eatnnovationApp/create_product.html"), name='createProduct'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Products o registro de la Base de Datos 
    path('productList/edit/<int:pk>', ProductUpdate.as_view(template_name = "eatnnovationApp/update_product.html"), name='updateProduct'), 
    # La ruta 'delete' que usaremos para delete un Products o registro de la Base de Datos 
    path('productList/delete/<int:pk>', ProductDelete.as_view(), name='deleteProduct'),


]
