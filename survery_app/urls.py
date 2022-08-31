from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.home),
  path('survey_arabic', views.survey_arabic, name='survey_arabic'),
  path('survey_english', views.survey_english, name='survey_english'),
  path('RIASEC_survey_arabic', views.RIASEC_survey_arabic, name='RIASEC_survey_arabic'),
  
]