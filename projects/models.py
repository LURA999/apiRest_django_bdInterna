# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class Autocapacitaciones(models.Model):
    idautocap = models.AutoField(db_column='idAutoCap', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=55)
    link = models.TextField()
    fechainicial = models.DateField(db_column='fechaInicial')  # Field name made lowercase.
    fechafinal = models.DateField(db_column='fechaFinal')  # Field name made lowercase.
    cvelocal = models.IntegerField(db_column='cveLocal')  # Field name made lowercase.




class Contrato(models.Model):
    idcontrato = models.AutoField(db_column='idContrato', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=25)


class EmpleadoMes(models.Model):
    idempleado_mes = models.AutoField(db_column='idEmpleado_mes', primary_key=True)  # Field name made lowercase.
    cveusuario = models.IntegerField(db_column='cveUsuario')  # Field name made lowercase.
    fecha = models.IntegerField()
    fechainicio = models.DateField(db_column='fechaInicio')  # Field name made lowercase.
    fechafinal = models.DateField(db_column='fechaFinal')  # Field name made lowercase.
    posicion = models.IntegerField()



class Imgvideo(models.Model):
    idimgvideo = models.AutoField(db_column='idImgVideo', primary_key=True)  # Field name made lowercase.
    fechainicial = models.DateField(db_column='fechaInicial')  # Field name made lowercase.
    fechafinal = models.DateField(db_column='fechaFinal')  # Field name made lowercase.
    imgvideo = models.CharField(db_column='imgVideo', max_length=150)  # Field name made lowercase.
    formato = models.CharField(max_length=15)
    cvelocal = models.IntegerField(db_column='cveLocal')  # Field name made lowercase.
    cveseccion = models.IntegerField(db_column='cveSeccion')  # Field name made lowercase.
    link = models.TextField(blank=True, null=True)
    posicion = models.IntegerField()




class Local(models.Model):
    idlocal = models.AutoField(db_column='idLocal', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=255)




class Menu(models.Model):
    idmenu = models.AutoField(db_column='idMenu', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    cvelocal = models.IntegerField(db_column='cveLocal')  # Field name made lowercase.
    fecha = models.DateField()




class Noticia(models.Model):
    idnoticia = models.AutoField(db_column='idNoticia', primary_key=True)  # Field name made lowercase.
    fechainicial = models.DateField(db_column='fechaInicial')  # Field name made lowercase.
    fechafinal = models.DateField(db_column='fechaFinal')  # Field name made lowercase.
    imgvideo = models.CharField(db_column='imgVideo', max_length=150)  # Field name made lowercase.
    formato = models.CharField(max_length=15)
    titulo = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=450)
    cvelocal = models.IntegerField(db_column='cveLocal')  # Field name made lowercase.
    link = models.TextField()
    activo = models.IntegerField()




class Secciones(models.Model):
    idseccion = models.AutoField(db_column='idSeccion', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=20)



class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    usuario = models.IntegerField()
    nombres = models.CharField(max_length=30)
    apellidopaterno = models.CharField(db_column='apellidoPaterno', max_length=25)  # Field name made lowercase.
    apellidomaterno = models.CharField(db_column='apellidoMaterno', max_length=25)  # Field name made lowercase.
    correo = models.CharField(max_length=55)
    contrasena = models.TextField()
    cverol = models.IntegerField(db_column='cveRol')  # Field name made lowercase.
    img = models.CharField(max_length=20)
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    fechaingreso = models.DateField(db_column='fechaIngreso')  # Field name made lowercase.
    departamento = models.CharField(max_length=35)
    contrato = models.IntegerField()



class Visitas(models.Model):
    idvisita = models.AutoField(db_column='idVisita', primary_key=True)  # Field name made lowercase.
    usuario = models.IntegerField()
    contador = models.IntegerField()
    fecha = models.DateTimeField()
