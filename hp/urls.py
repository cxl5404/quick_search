# 引入path
from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'hp'

urlpatterns = [
     path('switch-list_100/', views.switch_list_100, name='switch_list_100'),
     path('switch-detail_100/<int:id>/', views.switch_detail_100, name='switch_detail_100'),
]