from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Switch_100M
from django.db.models import Q

def switch_list_100(request):
    # 取出所有
    switches = Switch_100M.objects.all()
    category = 'HP/H3C 100M Transceiver Modules Lookup'
    # 需要传递给模板（templates）的对象
    context = { 'switches': switches, 
    'category': category }

    # render函数：载入模板，并返回context对象
    return render(request, 'hp/list.html', context)

def switch_detail_100(request, id):
    # 取出相应
    switch = Switch_100M.objects.get(id=id)
    # 需要传递给模板的对象
    context = { 'switch': switch }
    # 载入模板，并返回context对象
    return render(request, 'hp/detail.html', context)



