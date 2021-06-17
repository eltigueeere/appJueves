from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View
from django.utils.six import BytesIO
import qrcode


class QrTarjeta(TemplateView):

    template_name = "qr/qr.html"


class VerQr(View):


    def get(self, request, *args, **kwargs):
        #if request.user.is_authenticated:
        data = "https://www.mexinc.com.mx/recompensas/compra/" #+ str(request.user)
        img = qrcode.make(data)
        buf = BytesIO()		# BytesIO se da cuenta de leer y escribir bytes en la memoria
        img.save(buf)
        image_stream = buf.getvalue()
        return HttpResponse(image_stream, content_type="image/png")
        #else:
        #    return redirect('/accounts/login/')  