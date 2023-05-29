from django.urls import path
from .views import home, Menu, registro, order_confirmation
from  eatnnovationApp.views import ProductCreate,ProductDelete,ProductDetail,ProductList,ProductUpdate
from  eatnnovationApp.views import UserList,UserDetail, UserCreate, UserUpdate, UserDelete
from  eatnnovationApp.views import CategoryCreate,CategoryList,CategoryUpdate,CategoryDelete,InvoiceList

urlpatterns = [
    # Ruta principal home
    path('', home, name="home"),
    # Ruta para el registro
    path('registro/', registro, name='registro'),
    # Ruta para el menú
    path('menu/', Menu.as_view(template_name = "eatnnovationApp/menu.html"), name='menu'),

    # Rutas para el crud en Productos
    
    # La ruta 'leer' en donde listamos todos los registros o Products de la Base de Datos
    path('productList/', ProductList.as_view(), name='productList'),
    # La ruta 'details' en donde mostraremos una página con los details de un Products o registro 
    path('productList/detail/<int:pk>', ProductDetail.as_view(template_name = "eatnnovationApp/detail_product.html"), name='detailProduct'),
    # La ruta 'create' en donde mostraremos un formulario para create un nuevo Products o registro  
    path('productList/create', ProductCreate.as_view(template_name = "eatnnovationApp/createProduct.html"), name='createProduct'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Products o registro de la Base de Datos 
    path('productList/edit/<int:pk>', ProductUpdate.as_view(template_name = "eatnnovationApp/updateProduct.html"), name='updateProduct'), 
    # La ruta 'delete' que usaremos para delete un Products o registro de la Base de Datos 
    path('productList/delete/<int:pk>', ProductDelete.as_view(), name='deleteProduct'),

    # Rutas para el crud en Usuarios

    path('userList/', UserList.as_view(template_name = "eatnnovationApp/user_list.html"), name='userList'),
    path('userList/detail/<int:pk>', UserDetail.as_view(template_name = "eatnnovationApp/detail_user.html"), name='detailUser'),
    path('userList/create', UserCreate.as_view(template_name = "eatnnovationApp/create_user.html"), name='createUser'),
    path('userList/edit/<int:pk>', UserUpdate.as_view(template_name = "eatnnovationApp/update_user.html"), name='updateUser'), 
    path('userList/delete/<int:pk>', UserDelete.as_view(), name='deleteUser'),

    # Rutas para el crud en Categorías

    path('categoryList/', CategoryList.as_view(template_name = "eatnnovationApp/category_list.html"), name='categoryList'),
    path('categoryList/create', CategoryCreate.as_view(template_name = "eatnnovationApp/create_category.html"), name='createCategory'),
    path('categoryList/edit/<int:pk>', CategoryUpdate.as_view(template_name = "eatnnovationApp/update_category.html"), name='updateCategory'), 
    path('categoryList/delete/<int:pk>', CategoryDelete.as_view(), name='deleteCategory'),

    # Ruta para la lista de las facturas
    path('invoiceList/', InvoiceList.as_view(template_name = "eatnnovationApp/invoice_list.html"), name='invoiceList'),

    # Rutas para el order now y la factura generada
    path('orders/', Menu.as_view(template_name = "eatnnovationApp/orders.html"), name='orders'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
]
