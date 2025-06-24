from django.contrib.admin.views.decorators import staff_member_required
from .models import Visita, Trabajo, Product
from datetime import timedelta, date
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page


@cache_page(600)
def home(request):
    print("⚙️ Vista generada (sin caché)")
    trabajos = Trabajo.objects.order_by('-creado')[:6]  # Últimos 6 trabajos
    return render(request, 'home.html', {'trabajos': trabajos})


@cache_page(600)
def trabajos_lista(request):
    print("⚙️ Vista generada (sin caché)")
    trabajos_all = Trabajo.objects.order_by('-creado')
    paginator = Paginator(trabajos_all, 10)  # 10 trabajos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'trabajos_lista.html', {'page_obj': page_obj})


@cache_page(600)
def contac(request):
    print("⚙️ Vista generada (sin caché)")
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            contenido = f"Mensaje de {nombre} ({email}):\n\n{mensaje}"

            send_mail(
                subject="Nuevo mensaje de contacto",
                message=contenido,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Reinicia el formulario y pasa 'exito' para mostrar mensaje
            return render(request, 'contact.html', {'form': ContactForm(), 'exito': True})

    return render(request, 'contact.html', {'form': form})


@cache_page(600)
def product_list(request):
    print("⚙️ Vista generada (sin caché)")

    filtro = request.GET.get('filtro')  # 'menor', 'mayor', 'descuento'

    if filtro == 'menor':
        productos = Product.objects.all().order_by('price')
    elif filtro == 'mayor':
        productos = Product.objects.all().order_by('-price')
    elif filtro == 'descuento':
        productos = Product.objects.filter(descuento__gt=0).order_by('-descuento')
    else:
        productos = Product.objects.all().order_by('-id')  # recientes primero

    paginator = Paginator(productos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product_list.html', {
        'page_obj': page_obj,
        'filtro': filtro,
    })


@cache_page(600)
def services(request):
    print("⚙️ Vista generada (sin caché)")
    template = loader.get_template("services.html")
    return HttpResponse(template.render())


@staff_member_required
def analytics_dashboard(request):
    today = date.today()
    semana = today - timedelta(days=7)
    mes = today - timedelta(days=30)

    visitas_hoy = Visita.objects.filter(fecha=today).count()
    visitas_semana = Visita.objects.filter(fecha__gte=semana).count()
    visitas_mes = Visita.objects.filter(fecha__gte=mes).count()

    return render(request, 'admin/analytics_dashboard.html', {
        'visitas_hoy': visitas_hoy,
        'visitas_semana': visitas_semana,
        'visitas_mes': visitas_mes,
    })


def prueba_email(request):
    try:
        send_mail(
            subject="Prueba de correo",
            message="Este es un mensaje de prueba",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['herreriasoldaduraunio2025@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse("✅ Correo enviado correctamente.")
    except Exception as e:
        return HttpResponse(f"❌ Error al enviar: {str(e)}")
