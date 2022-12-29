from django.urls import path
from django.urls import path, include

#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.home),
  
  path('survey_arabic', views.survey_arabic, name='survey_arabic'),
  path('survey_arabic<str:link>', views.survey_arabic, name='survey_arabic'),
  path('survey_english', views.survey_english, name='survey_english'),

  path('<str:user_id>/<str:user_name>/arabic_confirmation', views.arabic_confirmation, name='arabic_confirmation'),
  path('<str:user_id>/<str:user_name>/arabic_2_confirmation', views.arabic_2_confirmation, name='arabic_2_confirmation'),
  path('<str:user_id>/<str:user_name>/arabic_3_confirmation', views.arabic_3_confirmation, name='arabic_3_confirmation'),
  path('<str:user_id>/<str:user_name>/arabic_4_confirmation', views.arabic_4_confirmation, name='arabic_4_confirmation'),
  path('<str:user_id>/<str:user_name>/after_survey_arabic', views.after_survey_arabic, name='after_survey_arabic'),
  path('<str:user_id>/<str:user_name>/download_report_page', views.download_report_page, name='download_report_page'),
  
  path('<str:user_id>/<str:user_name>/download_report_free', views.download_report_free, name='download_report_free'),
  path('<str:user_id>/<str:user_name>/download_report_paid', views.download_report_paid, name='download_report_paid'),
  path('<str:user_id>/<str:user_name>/paypal', views.paypal, name='paypal'),
  path('<str:user_id>/<str:user_name>/paypal_success', views.paypal_success, name='paypal_success'),
  path('<str:user_id>/<str:user_name>/c', views.c, name='c'),
  path('<str:user_id>/<str:user_name>/no_coupon', views.no_coupon, name='no_coupon'),
  path('<str:user_id>/<str:user_name>/coupon', views.coupon, name='coupon'),

  path('<str:user_id>/<str:user_name>/download_receipt', views.download_receipt, name='download_receipt'),

  path('RIASEC_survey_arabic', views.RIASEC_survey_arabic, name='RIASEC_survey_arabic'),
]