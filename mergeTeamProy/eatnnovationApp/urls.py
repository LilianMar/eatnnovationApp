from django.urls import path
from .views import home,Menu,registro
from  eatnnovationApp.views import ProductCreate,ProductDelete,ProductDetail,ProductList,ProductUpdate
from  eatnnovationApp.views import UserList,UserDetail, UserCreate, UserUpdate, UserDelete

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name='registro'),
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
    

    path('userList/', UserList.as_view(template_name = "eatnnovationApp/user_list.html"), name='userList'),
    path('userList/detail/<int:pk>', UserDetail.as_view(template_name = "eatnnovationApp/detail_user.html"), name='detailUser'),
    # La ruta 'create' en donde mostraremos un formulario para create un nuevo Products o registro  
    path('userList/create', UserCreate.as_view(template_name = "eatnnovationApp/create_user.html"), name='createUser'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Products o registro de la Base de Datos 
    path('userList/edit/<int:pk>', UserUpdate.as_view(template_name = "eatnnovationApp/update_user.html"), name='updateUser'), 
    # La ruta 'delete' que usaremos para delete un Products o registro de la Base de Datos 
    path('userList/delete/<int:pk>', UserDelete.as_view(), name='deleteUser'),

   
]
