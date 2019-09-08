from django.views.generic import *
from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import render
class HomePage(TemplateView):
    template_name='preneur.html'

class TestPage(TemplateView):
    template_name='test.html'

class ThanksPage(TemplateView):
    template_name='thanks.html'

class Arena1(TemplateView):
    template_name='arena1.html'
class Leaderboard(TemplateView):
    template_name='leaderboard.html'
    def get(self,request):
        if (request.method=='GET'):
            User=get_user_model()
            users=User.objects.all()
        return render(request, 'leaderboard.html', {'data': users})


class Redirection(TemplateView):
    template_name='homeredirect.html'
