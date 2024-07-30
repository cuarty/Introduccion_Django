from django.views.generic import View
from django.shortcuts import render

#Esta clase es una vista para poder verla a través del URL
class HomeView (View):
    def get (self, request, *args, **kwargs):
        context={

        }
        return render(request,'index.html',context)