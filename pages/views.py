from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def homePageView(request):
#     return HttpResponse('hello world')
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

def upload(request):
    context = {}

    if request.method == "POST":
        upfile = request.FILES["document"]

        context["fname"] = upfile.name
        context["fsize"] = upfile.size
        print(upfile.name)
        print(upfile.size)

    return render(request, "upload.html", context)