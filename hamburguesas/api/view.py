from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from hamburguesas.models import Hamburguesa
from hamburguesas.api.serializers import HamburguesaSerializer
from ingredientes.models import Ingrediente

    

@api_view(['GET','POST'])
def api_list_Hamburguesa_view(request):

    try:
        hamburguesa = Hamburguesa.objects.all()
    except Hamburguesa.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
       
    if request.method == "GET":        
        serializer = HamburguesaSerializer(hamburguesa, many=True, context={'request': request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = HamburguesaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    
  

@api_view(['GET', 'DELETE', 'PATCH'])
def api_detail_Hamburguesa_view(request, id):

    try:
        if not id.isdigit():            
            return Response({"id invalido"}, status = status.HTTP_400_BAD_REQUEST)
        hamburguesa = Hamburguesa.objects.get(id=id)
    except Hamburguesa.DoesNotExist:
        return Response({"Hamburguesa inexistente"}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = HamburguesaSerializer(hamburguesa)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "DELETE":
        operation = hamburguesa.delete()
        data={}
        if operation:
            data["success"]="Eliminado exitosamente"
            return Response(data = data, status = status.HTTP_200_OK)
        else:
            data["failure"] = "No se pudo eliminar"
            return Response(data = data, status = status.HTTP_404_NOT_FOUND)   

    elif request.method == "PATCH":       
        for key in request.data.keys():
            if key not in ["nombre", "descripcion", "precio", "imagen"]:
                return Response({"Parámetros inválidos"}, status = status.HTTP_400_BAD_REQUEST)
        serializer = HamburguesaSerializer(hamburguesa, data = request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
    
 

@api_view(['DELETE', 'PUT'])
def api_delete_Hamburguesa_Ingrediente_view(request, idh, idi):

    try:
        if not idh.isdigit() or not idi.isdigit():            
            return Response({"400_id_invalido"}, status = status.HTTP_400_BAD_REQUEST)
        if request.method == "DELETE":
            hamburguesa = Hamburguesa.objects.get(id=idh)                        
            ingrediente = hamburguesa.ingredientes.get(id=idi)              
 
        elif request.method == "PUT":
            hamburguesa = Hamburguesa.objects.get(id=idh)
            ingrediente = Ingrediente.objects.get(id=idi)       
    except (Hamburguesa.DoesNotExist,Ingrediente.DoesNotExist):
        return Response({"HTTP_404_NOT_FOUND"}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        hamburguesa.ingredientes.remove(ingrediente)
        data={}
        data["success"]="Eliminado exitosamente"
        return Response(data = data, status = status.HTTP_200_OK)
        
    elif request.method == "PUT":
        hamburguesa.ingredientes.add(ingrediente)
        serializer = HamburguesaSerializer(hamburguesa)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

        
    
    