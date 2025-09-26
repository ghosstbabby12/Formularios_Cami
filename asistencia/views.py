from django.shortcuts import render, redirect
from .forms import AsistenciaForm

def registrar_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion_asistencia')
    else:
        form = AsistenciaForm()
    return render(request, 'asistencia/formulario.html', {'form': form})

def confirmacion_asistencia(request):
    return render(request, 'asistencia/confirmacion.html')
