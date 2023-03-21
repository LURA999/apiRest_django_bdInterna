from projects.serializers import AutocapacitacionesSerializer,ContratoSerializer,EmpleadoMesSerializer,ImgvideoSerializer,LocalSerializer,MenuSerializer,NoticiaSerializer,SeccionesSerializer,UsuarioSerializer,VisitasSerializer
from .models import Autocapacitaciones, Contrato, EmpleadoMes, Imgvideo, Local, Menu, Noticia, Secciones, Usuario, Visitas
from rest_framework import viewsets, permissions


class AutocapacitacionesViewSet(viewsets.ModelViewSet):
    queryset = Autocapacitaciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AutocapacitacionesSerializer
    
class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ContratoSerializer
    
class EmpleadoMesViewSet(viewsets.ModelViewSet):
    queryset = EmpleadoMes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoMesSerializer
    
class ImgvideoViewSet(viewsets.ModelViewSet):
    queryset = Imgvideo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ImgvideoSerializer
    
class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LocalSerializer
    
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MenuSerializer
    
class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NoticiaSerializer
    
class SeccionesViewSet(viewsets.ModelViewSet):
    queryset = Secciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SeccionesSerializer
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer
    
class VisitasViewSet(viewsets.ModelViewSet):
    queryset = Visitas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VisitasSerializer
    