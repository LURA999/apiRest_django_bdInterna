from rest_framework import routers

from .views import AutocapacitacionesViewSet,ContratoViewSet,EmpleadoMesViewSet,ImgvideoViewSet,LocalViewSet,MenuViewSet,NoticiaViewSet,SeccionesViewSet,UsuarioViewSet,VisitasViewSet

router = routers.DefaultRouter()


router.register('api/autocapacitaciones',AutocapacitacionesViewSet,'autocapacitaciones')
router.register('api/contrato',ContratoViewSet,'contrato')
router.register('api/empleado',EmpleadoMesViewSet, 'empleado')
router.register('api/imgVideo',ImgvideoViewSet, 'imgVideo')
router.register('api/local',LocalViewSet, 'local')
router.register('api/menu',MenuViewSet, 'menu')
router.register('api/noticia',NoticiaViewSet, 'noticia')
router.register('api/seccion',SeccionesViewSet, 'seccion')
router.register('api/usuario',UsuarioViewSet, 'usuario')
router.register('api/visita',VisitasViewSet, 'visita')

urlpatterns = router.urls
