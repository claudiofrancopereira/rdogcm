from django.db import models
from django.utils import timezone

# Create your models here.

class RDO( models.Model ):
	
	numero = models.IntegerField()
	data = models.DateField()
	viatura = models.CharField( max_length = 50, default = None)
	guarnicao = models.CharField( max_length = 50 )
	hora_fato = models.TimeField( blank = True )
	hora_comunicacao = models.TimeField( blank = True )
	hora_local = models.TimeField()
	hora_final = models.TimeField()
	local = models.CharField( max_length = 100 )
	natureza = models.CharField( max_length = 50 )
	historico = models.TextField()
	
	
	#def __str__( self ):
	#	return str( self.numero ) + "/" + str( timezone.now().year )

