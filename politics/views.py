from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView
from politics.google_api_handler import ApiHandler
from politics.propublica_api_handler import ProPub_Api_Handler
from .models import Politician

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class RepPageView(View):
    template_name = 'myreps.html'


    def get(self, request):
        r = request.user
        if r.address2:
            address = r.address1 + " " + r.address2 + " " + r.city + " " +r.state + " " + r.zip_code
        else: 
            address = r.address1 + " " + r.city + " " +r.state + " " + r.zip_code
        GoogleHandler = ApiHandler("https://civicinfo.googleapis.com/civicinfo/v2/representatives?",address,"AIzaSyDprT-PBib6-i5eSdzWxDxVqckzfbyt9DI")
        politician_is = GoogleHandler.create_politician_list()

        return render(request, self.template_name, {'pol_list': politician_is})

class VoterRegView(TemplateView):
    template_name = 'voterreg.html'

class RepDetailView(DetailView):
    model = Politician
    template_name = 'rep_detail.html'

class UpcomingLegView(View):
    template_name = 'legislation.html'

    def get(self, request):
        house_handler = ProPub_Api_Handler("https://api.propublica.org/congress/v1/116/house/bills/introduced.json")
        senate_handler = ProPub_Api_Handler("https://api.propublica.org/congress/v1/116/senate/bills/introduced.json")
        house_list = house_handler.call_propub_api()
        senate_list = senate_handler.call_propub_api()

        return render(request, self.template_name, {'house_list': house_list,'senate_list': senate_list})
