from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from ingredientes.models import Ingrediente
from ingredientes.api.serializers import IngredienteSerializer
from hamburguesas.models import Hamburguesa

    

@api_view(['GET','POST'])
def api_list_Ingrediente_view(request):
    try:
        ingrediente = Ingrediente.objects.all()
    except Ingrediente.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
       
    if request.method == "GET":        
        serializer = IngredienteSerializer(ingrediente, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "POST":        
        serializer = IngredienteSerializer(data = request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
       

@api_view(['GET','DELETE'])
def api_detail_Ingrediente_view(request, id):

    try:
        if  not id.isdigit():
            return Response({"id invalido"}, status = status.HTTP_400_BAD_REQUEST)
        ingrediente = Ingrediente.objects.get(id=id)
    except Ingrediente.DoesNotExist:
        return Response({"Ingrediente inexistente"}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    if request.method == "DELETE":
        hamburguesas = Hamburguesa.objects.all()
        for hamburguesa in hamburguesas:
            ingredientes = hamburguesa.ingredientes.all()
            for ingrediente in ingredientes:
                if str(ingrediente.id) == id:
                    data={}
                    data["failure"] = "Ingrediente no se puede borrar, se encuentra presente en una hamburguesa"
                    return Response(data = data, status = status.HTTP_409_CONFLICT)
        operation = ingrediente.delete()
        data={}
        if operation:
            data["success"]="Eliminado exitosamente"
            return Response(data = data, status = status.HTTP_200_OK)
        else:
            data["failure"] = "No se pudo eliminar"
            return Response(data = data, status = status.HTTP_404_NOT_FOUND)

    

    
    



        
    
    