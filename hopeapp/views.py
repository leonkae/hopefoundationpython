from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse
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
        announcements = Announcements.objects.first()
        context ={
            "events":events,
            "letters":letters,
            "progs":progs,
            "teams":teams,
            "gals":gals,
            "vission":vission,
            "mission":mission,
            "about":about,
            "announcements":announcements
        }
        
        return render(request, self.template_name,context)
    
class DonateView(ListView):
    template_name = "hopeTemp/donation.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form_type = request.POST.get("form_type")

        if form_type == "donation":
            Donation.objects.create(
                name=request.POST.get("name"),
                phone_number=request.POST.get("phone_number"),
                mpesa_code=request.POST.get("mpesa_code"),
                email=request.POST.get("email"),
                amount=request.POST.get("amount")
            )
            return redirect("success_page")

        elif form_type == "volunteer":
            Volunteer.objects.create(
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                email=request.POST.get("email"),
                reason=request.POST.get("reason")
            )
            return redirect("success_page")

        elif form_type == "contact":
            ContactMessage.objects.create(
                name=request.POST.get("name"),
                phone_number=request.POST.get("phone_number"),
                email=request.POST.get("email"),
                message=request.POST.get("message")
            )
            return redirect("success_page")

        return redirect("error_page")

    
def success_page(request):
    return render(request, "hopeTemp/success.html")

def error_page(request):
    return render(request, "hopeTemp/error.html")