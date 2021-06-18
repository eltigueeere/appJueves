from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View
from django.utils.six import BytesIO
from django.shortcuts import redirect
import qrcode
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



@method_decorator(login_required, name='dispatch')
class QrTarjeta(TemplateView):
    template_name = "qr/qr.html"


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'nombreCard':str(request.user)})




class VerQr(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data = "https://www.mexinc.com.mx/rewards/compra/" + str(request.user)
            img = qrcode.make(data)
            buf = BytesIO()		# BytesIO se da cuenta de leer y escribir bytes en la memoria
            img.save(buf)
            image_stream = buf.getvalue()
            return HttpResponse(image_stream, content_type="image/png")
        else:
            return redirect('/accounts/login/')  