from django.urls import path

from ingredientes.api.view import (
api_detail_Ingrediente_view, 
api_list_Ingrediente_view,)


app_name = 'ingrediente'

urlpatterns = [
    path('ingrediente', api_list_Ingrediente_view, name= 'list'),
    path('ingrediente/<id>', api_detail_Ingrediente_view, name= 'ingrediente-detail'),
]