from django.views.generic import TemplateView

from .data_loader import load_data

class HomePageView(TemplateView):
    template_name='home.html'

class GMBuildsPageView(TemplateView):
    template_name='GMBuilds.html'

    load_data()

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context["god"] = {'name': 'Set', 'godIcon_URL':'https:\/\/web2.hirez.com\/smite\/god-icons\/set.jpg'}
        context["build"] = {
            'relics':[
                "https:\/\/web2.hirez.com\/smite\/item-icons\/purification-beads.jpg",
                "https:\/\/web2.hirez.com\/smite\/item-icons\/aegis-amulet-upgrade.jpg",
            ],
            'items':[
                "https:\/\/web2.hirez.com\/smite\/item-icons\/evolved-attackers-blessing.jpg",
                "https:\/\/web2.hirez.com\/smite\/item-icons\/blackthorn-hammer.jpg",
                "https:\/\/web2.hirez.com\/smite\/item-icons\/ninja-tabi.jpg",
                "https:\/\/web2.hirez.com\/smite\/item-icons\/frostbound-hammer.jpg",
                "https:\/\/web2.hirez.com\/smite\/item-icons\/runeforged-hammer.jpg",
                "https:\/\/web2.hirez.com\/smite\/item-icons\/qins-sais.jpg",
            ],
        }
        context["player"] = {'name': 'Unknown Player', 'Duel_Tier':'Platinum 2'}
        context["opponent"] = {'name': 'Unknown Player', 'godIcon_URL':"https:\/\/web2.hirez.com\/smite\/god-icons\/amaterasu.jpg"}
        return context