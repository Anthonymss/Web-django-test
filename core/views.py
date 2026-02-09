from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Producto
from .forms import ProductoForm, RegistroForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.conf import settings

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_productos')
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})

# Vistas de Productos CRUD

def lista_productos(request):
    productos_list = Producto.objects.all().order_by('-creado_at')
    paginator = Paginator(productos_list, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/lista_productos.html', {'page_obj': page_obj})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'core/formulario_producto.html', {'form': form, 'titulo': 'Crear Producto'})

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'core/formulario_producto.html', {'form': form, 'titulo': 'Editar Producto', 'producto': producto})

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'core/confirmar_eliminacion.html', {'producto': producto})
    return render(request, 'core/confirmar_eliminacion.html', {'producto': producto})

def exportar_pdf(request):
    productos = Producto.objects.all().order_by('categoria', 'nombre')
    template_path = 'core/catalogo_pdf.html'
    context = {'productos': productos}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="catalogo_productos.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    template = get_template(template_path)
    html = template.render(context)

    def link_callback(uri, rel):
        sUrl = settings.STATIC_URL
        sRoot = settings.STATIC_ROOT
        mUrl = settings.MEDIA_URL
        mRoot = settings.MEDIA_ROOT

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

        if not os.path.isfile(path):
            raise Exception(f'media URI must start with {sUrl} or {mUrl}')
        return path

    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def mantenimiento(request):
    return render(request, 'core/mantenimiento.html')
