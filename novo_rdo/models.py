from django.db import models
from django.utils import timezone

# Create your models here.

class RDO( models.Model ):
	numero = models.PositiveSmallIntegerField()
	data = models.DateField( auto_now=True )
	guarnicao = models.CharField( max_length = 50 )
	hora_fato = models.TimeField()
	hora_comunicacao = models.TimeField()
	hora_local = models.TimeField()
	hora_final = models.TimeField()
	local = models.CharField( max_length = 100 )
	natureza = models.CharField( max_length = 50 )
	historico = models.TextField()
	timestamp = models.DateField( auto_now_add=True )

	def __str__( self ):
		return str( self.numero ) + "/" + str( timezone.now().year )

