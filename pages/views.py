from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name='home.html'

class GMBuildsPageView(TemplateView):
    template_name='GMBuilds.html'