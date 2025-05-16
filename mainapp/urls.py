from django.urls import path
from . import views

urlpatterns = [
    path('upload_resume',views.upload_resume,name='upload_resume'),
    path('',views.home,name='home'),
    # path('second_views', views.second_views, name='second_views'),
    path('high_score_resumes/', views.high_score_resumes, name='high_score_resumes'),
]
