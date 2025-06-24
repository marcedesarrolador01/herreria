from .models import Visita
from datetime import date

class ContadorVisitasMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not request.path.startswith('/admin/') and not request.user.is_staff:
            ip = request.META.get('REMOTE_ADDR', None)
            Visita.objects.create(url=request.path, ip=ip)

        return response
