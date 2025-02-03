from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

class HomeView(ListView):
    template_name = "hopeTemp/index.html"
    
    def get(self, request):
        events = Events.objects.all()
        letters = Newsletter.objects.all()
        progs = Programmes.objects.all()
        teams =Team.objects.all()
        gals = Gallery.objects.all()
        vission = Vission.objects.first()
        mission = Mission.objects.first()
        about = About.objects.first()
        context ={
            "events":events,
            "letters":letters,
            "progs":progs,
            "teams":teams,
            "gals":gals,
            "vission":vission,
            "mission":mission,
            "about":about
        }
        
        return render(request, self.template_name,context)
    
