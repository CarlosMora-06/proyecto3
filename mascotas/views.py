from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from mascotas.models import Responsable
from mascotas.serializers import Mascota

##############MASCOTA##################

@api_view(['POST','PUT'])
def crear_mascota(request):
    datos_mascota_deserializado = MascotaSerializer(data=request.data)

    if datos_mascota_deserializado.is_valid(): # Validar básico
        datos_mascota_deserializado.save() # Guardar
        return Response(datos_mascota_deserializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(datos_mascota_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_mascotas(request):
    try:
        listado_mascota = Mascota.objects.all()  # SELECT * FROM cliente;
        serializado = MascotaSerializer(listado_mascota, many=True)  # Convertimos a JSON

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def modificar_mascota(request, id):
    try:
        mascota_seleccionado = Mascota.objects.get(id=id)
        serializado = MascotaSerializer(mascota_seleccionado, data=request.data) # request.data = datos modificados desde frontend

        if serializado.is_valid(): # Verifica si cumple con los datos básicos
            serializado.save()
            return Response(serializado.data, status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminar_mascota(request, id):
    try:
        mascota_obtenido = Mascota.objects.get(id=id)
        mascota_obtenido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

########RESPONSABLE#################



@api_view(['POST','PUT'])
def crear_responsable(request):
    datos_responsable_deserializado = MascotaSerializer(data=request.data)
    try:

        if datos_responsable_deserializado.is_valid(): # Validar básico
            datos_responsable_deserializado.save() # Guardar
            return Response(datos_responsable_deserializado.data, status=status.HTTP_201_CREATED)
        else:
            return Response(datos_responsable_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_responsables(request):
    try:

        serializado = ResponsableSerializer(listado_responsable, many=True)  # Convertimos a JSON

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def modificar_responsable(request, id):
    try:
        responsable_seleccionado = Responsable.objects.get(id=id)
        serializado = ResponsableSerializer(responsable_seleccionado, data=request.data) # request.data = datos modificados desde frontend

        if serializado.is_valid(): # Verifica si cumple con los datos básicos
            serializado.save()
            return Response(serializado.data, status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_responsable(request, id):
    try:
        responsable_obtenido = Responsable.objects.get(id=id)
        responsable_obtenido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)



