from rest_framework import serializers
from .models import Autocapacitaciones, Contrato, EmpleadoMes, Imgvideo, Local, Menu, Noticia, Secciones, Usuario, Visitas

    
class AutocapacitacionesSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Autocapacitaciones
        fields = ('idautocap', 'nombre', 'link', 'fechainicial','fechafinal','cvelocal')
        
class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ('idcontrato', 'nombre')
        
class EmpleadoMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpleadoMes
        fields = ('idempleado_mes', 'cveusuario', 'fecha', 'fechainicio','fechafinal','posicion')
        
class ImgvideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imgvideo
        fields = ('idimgvideo','fechainicial','fechafinal','imgvideo','formato','cvelocal','cveseccion','link','posicion')
        
class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ('idlocal','nombre','ubicacion')
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('idmenu','nombre','descripcion','cvelocal','fecha')
        
class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ('idnoticia','fechainicial','fechafinal','imgvideo','formato','titulo','descripcion','cvelocal','link','activo')
        
class SeccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secciones
        fields = ('idseccion','nombre')
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('idusuario','usuario','nombres','apellidopaterno','apellidomaterno','correo','contrasena','cverol','img','fechanacimiento','fechaingreso','departamento','contrato')
        
class VisitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitas
        fields = ('idvisita','usuario','contador','fecha',)
