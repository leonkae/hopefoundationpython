from django.shortcuts import render
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
    
class DonateView(ListView):
    template_name = "hopeTemp/donation.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form_type = request.POST.get("form_type")

        if form_type == "donate":
            name = request.POST.get("name")
            phone_number = request.POST.get("phone_number")
            mpesa_code = request.POST.get("mpesa_code")
            email = request.POST.get("email")
            amount = request.POST.get("amount")

            Donation.objects.create(
                name=name,
                phone_number=phone_number,
                mpesa_code=mpesa_code,
                email=email,
                amount=amount
            )
            return JsonResponse({"success": True, "message": "Donation submitted successfully"})

        elif form_type == "volunteer":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            reason = request.POST.get("reason")

            Volunteer.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                reason=reason
            )
            return JsonResponse({"success": True, "message": "Volunteer application submitted successfully"})

        elif form_type == "contact":
            name = request.POST.get("name")
            phone_number = request.POST.get("phone_number")
            email = request.POST.get("email")
            message = request.POST.get("message")

            ContactMessage.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                message=message
            )
            return JsonResponse({"success": True, "message": "Message sent successfully"})

        return JsonResponse({"success": False, "message": "Invalid request"})
