from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('result/<int:pk>/', views.ResultView.as_view(), name='result'),
    path('history/', views.HistoryView.as_view(), name='history')
]
