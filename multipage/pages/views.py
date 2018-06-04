from django.shortcuts import HttpResponse, render
from pages import models


# Create your views here.

def user_list(request):
        result = models.UserList.objects.all()
        return render(request, 'page_list.html', {'result': result})