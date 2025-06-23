from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from .models import Article
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

class RestrictedListView(PermissionRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"
    permission_required = 'lek5.can_publish'
    context_object_name = 'articles'