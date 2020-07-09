from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return HttpResponse('Hello World')

def hello(request):
    return render(request,"hello/hello.html")

class MemberList(TemplateView):
    template_name = 'hello/hello.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'こんにちは'
        return context