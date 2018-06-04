from django.shortcuts import HttpResponse, render
from pages import models


# Create your views here.

from django.shortcuts import render
from django.shortcuts import HttpResponse
from pages import models


# Create your views here.


class Pager(object):
    def __init__(self, current_page):
        self.current_page = int(current_page)
        # 把方法伪造成属性(1)

    @property
    def start(self):
        return (self.current_page - 1) * 10

    @property
    def end(self):
        return self.current_page * 10


def user_list(request):
    current_page = request.GET.get('page', 1)
    page_obj = Pager(current_page)
    # 把方法改造成属性(2),这样在下面调用方法的时候就不需要加括号了
    result = models.UserList.objects.all()[page_obj.start:page_obj.end]
    return render(request, 'page_list.html', {'result': result})