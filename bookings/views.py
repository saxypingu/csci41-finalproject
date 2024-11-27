# views.py
from django.views import View
from django.http import HttpResponse

class TestView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("This is a GET response from the GenericView!", content_type="text/plain")

    def post(self, request, *args, **kwargs):
        return HttpResponse("POST requests are not yet implemented.", content_type="text/plain", status=400)
    
# Create your views here.