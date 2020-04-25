from rest_framework import serializers
from hamburguesas.models import Hamburguesa
from ingredientes.api.serializers import IngredienteSerializer


class HamburguesaSerializer(serializers.ModelSerializer):
    ingredientes = serializers.SerializerMethodField()

    def get_ingredientes(self, hamburguesa):
        lista = []  
        url = "tarea-2-api-nacrur.herokuapp.com/ingrediente/"
        for ingrediente in hamburguesa.ingredientes.all():
            dicto = dict()
            id = ingrediente.id
            url1 = url+str(id)
            dicto["path"]= url1
            lista.append(dicto)
            #print(f"INGREDIENTEEE: {id}")           

        return lista
    # ingredientes = serializers.HyperlinkedRelatedField(many=True,
    #                                         read_only=True,
    #                                         view_name='ingredientes:ingrediente-detail',) 
    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre','precio', 'descripcion','imagen','ingredientes']