from django.shortcuts import render
from .forms import RDOForm
from .models import RDO
import datetime

def novo_rdo( request ):
	fRDO = RDOForm()
	iNumero = (RDO.objects.count() + 1)
	dData = datetime.date.today()
	
	if request.method == 'POST':
		fRDO = RDOForm( request.POST )

		if fRDO.is_valid():
			RDO.objects.create( numero = iNumero, 
								data = dData, 
								**fRDO.cleaned_data )
			fRDO = RDOForm()
			iNumero = (RDO.objects.count() + 1)
	
	context = { 'numero': iNumero,
				'data': format( dData, '%d/%m/%y' ),
				'ano': datetime.date.today().year,
				'form': fRDO }

	return render( request, "novo_rdo.html", context )

# Create your views here.
