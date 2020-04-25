from django.urls import path, include

from hamburguesas.api.view import (
api_detail_Hamburguesa_view, 
api_list_Hamburguesa_view,
api_delete_Hamburguesa_Ingrediente_view,)


app_name = 'hamburguesa'

urlpatterns = [
    path('hamburguesa', api_list_Hamburguesa_view, name= 'list'),
    path('hamburguesa/<id>', api_detail_Hamburguesa_view, name= 'detail'),
    path('hamburguesa/<idh>/ingrediente/<idi>', api_delete_Hamburguesa_Ingrediente_view, name = 'delete_ingre')
]