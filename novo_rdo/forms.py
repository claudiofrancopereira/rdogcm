from django import forms
from .models import RDO

import datetime

class RDOForm( forms.Form ):
	#numero = forms.IntegerField( initial = (RDO.objects.count() + 1), disabled = True )
	
	# data = forms.DateField( initial = datetime.date.today, 
	# 						widget = forms.DateInput( format = '%d/%m/%Y' ),
	# 						disabled = True)
	
	viatura = forms.CharField()
	guarnicao = forms.CharField()
	hora_fato = forms.TimeField( required = False )
	hora_comunicacao = forms.TimeField( required = False )
	hora_local = forms.TimeField()
	hora_final = forms.TimeField()
	local = forms.CharField()
	natureza = forms.CharField()
	historico = forms.CharField( widget = forms.Textarea() )

	