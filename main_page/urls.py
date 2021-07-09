from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='main_page'),
    path('privacy_policy/',views.privacy_policy,name='privacy_policy'),
    path('exams/',views.exams,name='exams'),
    path('exam_subpage/',views.exam_subpage,name='exam_subpage'),
    path('about_us/',views.about_us,name='about_us'),
    path('hof_army/',views.hof_army,name='hof_army'),
]
