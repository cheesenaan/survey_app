from django.urls import path
from django.urls import path, include

#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.home),
  path('survey_arabic', views.survey_arabic, name='survey_arabic'),
  path('survey_english', views.survey_english, name='survey_english'),

  path('arabic_confirmation', views.arabic_confirmation, name='arabic_confirmation'),
  path('arabic_2_confirmation', views.arabic_2_confirmation, name='arabic_2_confirmation'),
  path('arabic_3_confirmation', views.arabic_3_confirmation, name='arabic_3_confirmation'),
  path('arabic_4_confirmation', views.arabic_4_confirmation, name='arabic_4_confirmation'),
  path('after_survey_arabic', views.after_survey_arabic, name='after_survey_arabic'),
  path('download_report_page', views.download_report_page, name='download_report_page'),
  path('download_report_free', views.download_report_free, name='download_report_free'),
  path('download_report_paid', views.download_report_paid, name='download_report_paid'),
  path('paypal', views.paypal, name='paypal'),
  

  path('RIASEC_survey_arabic', views.RIASEC_survey_arabic, name='RIASEC_survey_arabic'),
]