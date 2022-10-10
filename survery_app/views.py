from contextlib import _RedirectStream
from datetime import datetime
import email
from fileinput import filename
import mimetypes
from multiprocessing import context
import os
import re
from unicodedata import name
from xml.etree.ElementTree import tostring
from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
from fpdf import FPDF
from django.shortcuts import redirect
import datetime

# Create your views here.
def home(request):
  return render(request, "home.html")

def RIASEC_survey_arabic(request):
      return render(request, "RIASEC_survey_arabic.html")


def survey_arabic(request):
    if request.method == 'POST':
        #print(request.POST)
        questions=question.objects.all()  

        # get user name and email
        if request.POST.get("user_name") == "":
          return render(request, "name_and_email.html")
          
        if request.POST.get("user_email") == "":
          return render(request, "name_and_email.html")

        user_name = request.POST.get("user_name")
        user_email = request.POST.get("user_email")
        user_phone = request.POST.get("user_phone")
        

        affinity_1 = 0
        affinity_2 = 0
        collection_1 = 0
        collection_2 = 0
        make_1 = 0
        make_2 = 0
        time_1 = 0
        time_2 = 0

        affinity_1_heading = ""
        affinity_2_heading = ""
        collection_1_heading = ""
        collection_2_heading = ""
        make_1_heading = ""
        make_2_heading = ""
        time_1_heading = ""
        time_2_heading = ""

        # get user response from form.
        for q in questions:
            if   request.POST.get(q.question_arabic_سؤال_عربي) == 'option1':
              if q.group_مجموعة == 'Affinity':    
                affinity_1 = affinity_1 + q.rank_النقاط
                affinity_1_heading = q.title_of_answer_choice_one_عنوان_الإجابة_الأول

              if q.group_مجموعة == 'Collection of information':    
                collection_1 = collection_1 + q.rank_النقاط
                collection_1_heading = q.title_of_answer_choice_one_عنوان_الإجابة_الأول
                
              if q.group_مجموعة == 'Make decision':    
                make_1 = make_1 + q.rank_النقاط
                make_1_heading = q.title_of_answer_choice_one_عنوان_الإجابة_الأول

              if q.group_مجموعة == 'Time spending':    
                time_1 = time_1 + q.rank_النقاط
                time_1_heading = q.title_of_answer_choice_one_عنوان_الإجابة_الأول

            if   request.POST.get(q.question_arabic_سؤال_عربي) == 'option2':
              if q.group_مجموعة == 'Affinity':    
                affinity_2 = affinity_2 + q.rank_النقاط
                affinity_2_heading = q.title_of_answer_choice_two_عنوان_الإجابة_الثاني

              if q.group_مجموعة == 'Collection of information':    
                collection_2 = collection_2 + q.rank_النقاط
                collection_2_heading = q.title_of_answer_choice_two_عنوان_الإجابة_الثاني
                
              if q.group_مجموعة == 'Make decision':    
                make_2 = make_2 + q.rank_النقاط
                make_2_heading = q.title_of_answer_choice_two_عنوان_الإجابة_الثاني

              if q.group_مجموعة == 'Time spending':    
                time_2 = time_2 + q.rank_النقاط
                time_2_heading = q.title_of_answer_choice_two_عنوان_الإجابة_الثاني
              
            if   request.POST.get(q.question_arabic_سؤال_عربي) == None:
              return render(request,'incomplete_survey.html')
            


        affinity_result = ""
        if affinity_1 > affinity_2:
          affinity_result = affinity_1_heading
        else:
          affinity_result = affinity_2_heading

        collection_result = ""
        if collection_1 > collection_2:
          collection_result = collection_1_heading
        else:
          collection_result = collection_2_heading

        make_result = ""
        if make_1 > make_2:
          make_result = make_1_heading
        else:
          make_result = make_2_heading

        time_result = ""
        if time_1 > time_2:
          time_result = time_1_heading
        else:
          time_result = time_2_heading
      

        
        if affinity_result == affinity_1_heading and collection_result == collection_1_heading and make_result == make_1_heading and time_result == time_1_heading :
              pdf_answer_case = 1
        elif affinity_result == affinity_1_heading and collection_result == collection_1_heading and make_result == make_1_heading and time_result == time_2_heading :
              pdf_answer_case = 2
        elif affinity_result == affinity_1_heading and collection_result == collection_1_heading and make_result == make_2_heading and time_result == time_1_heading :
          pdf_answer_case = 3
        elif affinity_result == affinity_1_heading and collection_result == collection_1_heading and make_result == make_2_heading and time_result == time_2_heading :
          pdf_answer_case = 4
        elif affinity_result == affinity_1_heading and collection_result == collection_2_heading and make_result == make_1_heading and time_result == time_1_heading :
          pdf_answer_case = 5
        elif affinity_result == affinity_1_heading and collection_result == collection_2_heading and make_result == make_1_heading and time_result == time_2_heading :
          pdf_answer_case = 6
        elif affinity_result == affinity_1_heading and collection_result == collection_2_heading and make_result == make_2_heading and time_result == time_1_heading :
          pdf_answer_case = 7
        elif affinity_result == affinity_1_heading and collection_result == collection_2_heading and make_result == make_2_heading and time_result == time_2_heading :
          pdf_answer_case = 8
        elif affinity_result == affinity_2_heading and collection_result == collection_1_heading and make_result == make_1_heading and time_result == time_1_heading :
          pdf_answer_case = 9
        elif affinity_result == affinity_2_heading and collection_result == collection_1_heading and make_result == make_1_heading and time_result == time_2_heading :
          pdf_answer_case = 10
        elif affinity_result == affinity_2_heading and collection_result == collection_1_heading and make_result == make_2_heading and time_result == time_1_heading :
          pdf_answer_case = 11
        elif affinity_result == affinity_2_heading and collection_result == collection_1_heading and make_result == make_2_heading and time_result == time_2_heading :
          pdf_answer_case = 12
        elif affinity_result == affinity_2_heading and collection_result == collection_2_heading and make_result == make_1_heading and time_result == time_1_heading :
          pdf_answer_case = 13
        elif affinity_result == affinity_2_heading and collection_result == collection_2_heading and make_result == make_1_heading and time_result == time_2_heading :
          pdf_answer_case = 14
        elif affinity_result == affinity_2_heading and collection_result == collection_2_heading and make_result == make_2_heading and time_result == time_1_heading :
          pdf_answer_case = 15
        elif affinity_result == affinity_2_heading and collection_result == collection_2_heading and make_result == make_2_heading and time_result == time_2_heading :
          pdf_answer_case = 16

        
        # put results in result model
        #result.objects.all().delete()
        r = result(
          time = request.POST.get('timer'),

          affinity_1 = affinity_1,
          affinity_2 = affinity_2,
          affinity_result= affinity_result,

          collection_1 = collection_1,
          collection_2 = collection_2,
          collection_result = collection_result,

          make_1 = make_1,
          make_2 = make_2,
          make_result = make_result,

          time_1 = time_1,
          time_2 = time_2,
          time_result = time_result,

          pdf_answer_case = pdf_answer_case,

          user_name = request.POST.get("user_name"),
          user_email = request.POST.get("user_email"),
          user_phone = request.POST.get("user_phone"),
          date_and_time_completed = datetime.datetime.now()
          )
        r.save()
        r_id = r.id

        context = {
          'affinity_result': affinity_result , 
          'collection_result': collection_result ,
          'make_result': make_result,
          'time_result': time_result,
          'user_email': user_email,
          'user_phone': user_phone,
          'id' : r_id

        }

        # render confirmation page
        return redirect('arabic_confirmation')


    else:
        questions=question.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'survey_arabic.html',context)
  

def survey_english(request):
    if request.method == 'POST':
        #print(request.POST)
        questions=question.objects.all()
        if   request.POST.get(name) == None:
              return render(request,'name_and_email.html')
        else:
          user_name = request.POST.get(name)

        
        if   request.POST.get(email) == None:
          return render(request,'name_and_email.html')
        else:
              email = request.POST.get(email)

        affinity_1 = 0
        affinity_2 = 0
        collection_1 = 0
        collection_2 = 0
        make_1 = 0
        make_2 = 0
        time_1 = 0
        time_2 = 0

        affinity_1_heading = ""
        affinity_2_heading = ""
        collection_1_heading = ""
        collection_2_heading = ""
        make_1_heading = ""
        make_2_heading = ""
        time_1_heading = ""
        time_2_heading = ""

        for q in questions:
            if   request.POST.get(q.question_english_سؤال_الانجليزي) == 'option1':
              if q.group_مجموعة == 'Affinity':    
                affinity_1 = affinity_1 + q.rank_النقاط
                affinity_1_heading = q.title_of_answer_choice_one_عنوان_الإجابة_الأول

              if q.group_مجموعة == 'Collection of Information':    
                collection_1 = collection_1 + q.rank_النقاط
                collection_1_heading = q.title_of_answer_choice_one_عنوان_الإجابة_الأول
                
              if q.group_مجموعة == 'Make decison':    
                make_1 = make_1 + q.rank_النقاط
                make_1_heading = q.title_of_answer_choice_one_عنوان_الإجابة_الأول

              if q.group_مجموعة == 'Time spending':    
                time_1 = time_1 + q.rank_النقاط
                time_1_heading = q.title_of_answer_choice_one_عنوان_الإجابة_الأول

            if   request.POST.get(q.question_english_سؤال_الانجليزي) == 'option2':
              if q.group_مجموعة == 'Affinity':    
                affinity_2 = affinity_2 + q.rank_النقاط
                affinity_2_heading = q.title_of_answer_choice_two_عنوان_الإجابة_الثاني

              if q.group_مجموعة == 'Collection of Information':    
                collection_2 = collection_2 + q.rank_النقاط
                collection_2_heading = q.title_of_answer_choice_two_عنوان_الإجابة_الثاني
                
              if q.group_مجموعة == 'Make decison':    
                make_2 = make_2 + q.rank_النقاط
                make_2_heading = q.title_of_answer_choice_two_عنوان_الإجابة_الثاني

              if q.group_مجموعة == 'Time spending':    
                time_2 = time_2 + q.rank_النقاط
                time_2_heading = q.title_of_answer_choice_two_عنوان_الإجابة_الثاني
            
            if   request.POST.get(q.question_english_سؤال_الانجليزي) == None:
                return render(request,'incomplete_survey.html')

            

            print("this is the request : ")
            print(request.POST.get(q.question_english_سؤال_الانجليزي))
            print()
        
        affinity_result = ""
        if affinity_1 > affinity_2:
          affinity_result = affinity_1_heading
        else:
          affinity_result = affinity_2_heading

        collection_result = ""
        if collection_1 > collection_2:
          collection_result = collection_1_heading
        else:
          collection_result = collection_2_heading

        make_result = ""
        if make_1 > make_2:
          make_result = make_1_heading
        else:
          make_result = make_2_heading

        time_result = ""
        if time_1 > time_2:
          time_result = time_1_heading
        else:
          time_result = time_2_heading
      

        
        if affinity_result == affinity_1_heading and collection_result == collection_1_heading and make_result == make_1_heading and time_result == time_1_heading :
              pdf_answer_case = 1
        elif affinity_result == affinity_1_heading and collection_result == collection_1_heading and make_result == make_1_heading and time_result == time_2_heading :
              pdf_answer_case = 2
        elif affinity_result == affinity_1_heading and collection_result == collection_1_heading and make_result == make_2_heading and time_result == time_1_heading :
          pdf_answer_case = 3
        elif affinity_result == affinity_1_heading and collection_result == collection_1_heading and make_result == make_2_heading and time_result == time_2_heading :
          pdf_answer_case = 4
        elif affinity_result == affinity_1_heading and collection_result == collection_2_heading and make_result == make_1_heading and time_result == time_1_heading :
          pdf_answer_case = 5
        elif affinity_result == affinity_1_heading and collection_result == collection_2_heading and make_result == make_1_heading and time_result == time_2_heading :
          pdf_answer_case = 6
        elif affinity_result == affinity_1_heading and collection_result == collection_2_heading and make_result == make_2_heading and time_result == time_1_heading :
          pdf_answer_case = 7
        elif affinity_result == affinity_1_heading and collection_result == collection_2_heading and make_result == make_2_heading and time_result == time_2_heading :
          pdf_answer_case = 8
        elif affinity_result == affinity_2_heading and collection_result == collection_1_heading and make_result == make_1_heading and time_result == time_1_heading :
          pdf_answer_case = 9
        elif affinity_result == affinity_2_heading and collection_result == collection_1_heading and make_result == make_1_heading and time_result == time_2_heading :
          pdf_answer_case = 10
        elif affinity_result == affinity_2_heading and collection_result == collection_1_heading and make_result == make_2_heading and time_result == time_1_heading :
          pdf_answer_case = 11
        elif affinity_result == affinity_2_heading and collection_result == collection_1_heading and make_result == make_2_heading and time_result == time_2_heading :
          pdf_answer_case = 12
        elif affinity_result == affinity_2_heading and collection_result == collection_2_heading and make_result == make_1_heading and time_result == time_1_heading :
          pdf_answer_case = 13
        elif affinity_result == affinity_2_heading and collection_result == collection_2_heading and make_result == make_1_heading and time_result == time_2_heading :
          pdf_answer_case = 14
        elif affinity_result == affinity_2_heading and collection_result == collection_2_heading and make_result == make_2_heading and time_result == time_1_heading :
          pdf_answer_case = 15
        elif affinity_result == affinity_2_heading and collection_result == collection_2_heading and make_result == make_2_heading and time_result == time_2_heading :
          pdf_answer_case = 16

        pdf_file_name = str(pdf_answer_case) + '.pdf'
        path_name = 'PDF/' + pdf_file_name

        pdf = FPDF()
        # Add a page
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = "welcome to your report", ln = 1, align = 'C')
        
        # add another cell
        pdf.cell(200, 10, txt = "this is the free version", ln = 2, align = 'C')

        pdf.cell(200, 10, txt = 'according to the affinity group, you are : ' +  affinity_result , ln = 2, align = 'L')
        pdf.cell(200, 10, txt = 'according to the collection of information group, you are : ' + collection_result , ln = 2, align = 'L')
        pdf.cell(200, 10, txt = 'according to the make decision group, you are : ' + make_result , ln = 2, align = 'L')
        pdf.cell(200, 10, txt = 'according to the time spending group, you are : ' + time_result , ln = 2, align = 'L')

        
        # save the pdf with name .pdf
        pdf.output(pdf_file_name) 
        pdf = pdf_file_name


        
        context = {
            'time': request.POST.get('timer'),

            'affinity_1':affinity_1,
            'affinity_2':affinity_2,
            'affinity_result':affinity_result,

            'collection_1' :collection_1,
            'collection_2' :collection_2,
            'collection_result':collection_result,

            'make_1' :make_1,
            'make_2':make_2,
            'make_result':make_result,

            'time_1':time_1,
            'time_2':time_2,
            'time_result':time_result,

            'pdf_answer_case':pdf_answer_case,
            'pdf_file_name':pdf_file_name,

        }


        return render(request,'after_survey_english.html',context)


    else:
        questions=question.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'survey_english.html',context)
  

def arabic_confirmation(request):
  user_result = result.objects.latest('id') 
  if request.method == 'POST':
    x = group_choice_change.objects.latest('id') 
    if request.POST.get("affinity_result") == "option2":
      if user_result.affinity_result == "Extrovert":
        user_result.affinity_result = "Introvert"
        x.affinity_Extrovert_to_Introvert = x.affinity_Extrovert_to_Introvert + 1
      else:
        user_result.affinity_result = "Extrovert"
        x.affinity_Introvert_to_Extrovert = x.affinity_Introvert_to_Extrovert + 1
    user_result.save()
    x.save()
  
    return redirect('arabic_2_confirmation')

  if request.method == 'GET':
    change = ""
    if  user_result.affinity_result == "Extrovert":
          change = change + "Introvert"
    else:
          change = change + "Extrovert"
    context = {
      "affinity_result": user_result.affinity_result,
      "change_result": change
    }
    return render(request , 'arabic_confirmation.html' , context)


def arabic_2_confirmation(request):
  user_result = result.objects.latest('id') 
  if request.method == 'POST':
    x = group_choice_change.objects.latest('id') 
    if request.POST.get("collection_result") == "option2":
      if user_result.collection_result == "Sensing":
        user_result.collection_result = "Intuition"
        x.collection_Sensing_to_Intuition = x.collection_Sensing_to_Intuition + 1
      else:
        user_result.collection_result = "Sensing"
        x.collection_Intuition_to_Sensing = x.collection_Intuition_to_Sensing + 1
    user_result.save()
    x.save()

    return redirect('arabic_3_confirmation')

  if request.method == 'GET':
    change = ""
    if  user_result.collection_result == "Sensing":
          change = change + "Intuition"
    if user_result.collection_result == "Intuition":
          change = change + "Sensing"

    context = {
      "collection_result" : user_result.collection_result,
      "change_result": change
    }
    return render(request , 'arabic_2_confirmation.html' , context)


def arabic_3_confirmation(request):
  user_result = result.objects.latest('id') 
  if request.method == 'POST':
    x = group_choice_change.objects.latest('id') 
    if request.POST.get("make_result") == "option2":
      if user_result.make_result == "Thinking":
        user_result.make_result = "Feeling"
        x.make_Thinking_to_Feeling = x.make_Thinking_to_Feeling + 1
      else:
        user_result.make_result = "Thinking"
        x.make_Feeling_to_Thinking = x.make_Feeling_to_Thinking + 1
    user_result.save()
    x.save()

    return redirect('arabic_4_confirmation')

  if request.method == 'GET':
        
    change = ""
    if  user_result.make_result == "Feeling":
          change = change + "Thinking"
    else:
          change = change + "Feeling"  

    context = {
      "make_result" : user_result.make_result,
      "change_result" : change
    }
    return render(request , 'arabic_3_confirmation.html' , context)


def arabic_4_confirmation(request):
  user_result = result.objects.latest('id') 
  if request.method == 'POST':
    x = group_choice_change.objects.latest('id') 
    if request.POST.get("time_result") == "option2":
      if user_result.time_result == "Judging":
        user_result.time_result = "Perceiving"
        x.time_Judging_to_Perceiving = x.time_Judging_to_Perceiving + 1
      else:
        user_result.time_result = "Judging"
        x.time_Perceiving_to_Judging = x.time_Perceiving_to_Judging + 1
    user_result.save()
    x.save()

    return redirect('after_survey_arabic')

  if request.method == 'GET':
        

    change = ""
    if  user_result.time_result == "Judging":
          change = change + "Perceiving"
    else:
          change = change + "Judging"  

    context = {
      "time_result" : user_result.time_result,
      "change_result" : change
    }
    return render(request , 'arabic_4_confirmation.html' , context)


def after_survey_arabic(request ):
  
      
   if request.method == 'POST':
        return redirect('download_report_page')
  
   if request.method == 'GET':

    r = result.objects.latest('id') 
    four_letter_code = ""

    # for some reason, Intuition is not I but N in the pdf drive.
    if r.collection_result[0] == "S":    
      four_letter_code = four_letter_code + r.affinity_result[0] + r.collection_result[0] + r.make_result[0] + r.time_result[0]

    if r.collection_result[0] == "I":    
        four_letter_code = four_letter_code + r.affinity_result[0] + "N" + r.make_result[0] + r.time_result[0]

    r.four_letter_code = four_letter_code
    r.save()

    pdf_free = ""
    pdf_free = pdf_free + four_letter_code + "_Free.pdf"
    r.pdf_free = pdf_free

    pdf_paid = ""
    pdf_paid = pdf_paid + four_letter_code + "_Full.pdf"
    r.pdf_paid = pdf_paid
    r.save()

    #print(pdf_free)

    #download pdf file
        
    context = {
                'time': r.time,

                'affinity_1': r.affinity_1 ,
                'affinity_2':r.affinity_2,
                'affinity_result':r.affinity_result,

                'collection_1' :r.collection_1,
                'collection_2' :r.collection_2,
                'collection_result':r.collection_result,

                'make_1' :r.make_1,
                'make_2':r.make_2,
                'make_result':r.make_result,

                'time_1':r.time_1,
                'time_2':r.time_2,
                'time_result':r.time_result,

                'pdf_answer_case':r.pdf_answer_case,
                'four_letter_code': four_letter_code

                  }
      
    return render(request, "after_survey_arabic.html" , context)


def download_report_page(request):
          
  if request.method == 'GET':
      # Load the template
      return render(request, 'download_report.html')

def download_report_free(request):
          from django.conf import settings
          r = result.objects.latest('id') 
          filename = r.pdf_free
          print()
          print(settings.BASE_DIR)
          print()
          filepath =  str(settings.BASE_DIR) + "/survery_app/PDF/" + str(filename)
          
          print(filepath)
          #path = open(filepath, 'rb')

          # importing required modules 
          import PyPDF2 

          # creating a pdf file object 
          pdfFileObj = open(filepath, 'rb') 

          # creating a pdf reader object 
          pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

          # creating a page object 
          pageObj = pdfReader.getPage(0) 
          print()
          print(pageObj.extractText()) 
          pdfFileObj.close() 

          path = open(filepath, 'rb')
          # Set the mime type
          mime_type, _ = mimetypes.guess_type(filepath)
          # Set the return value of the HttpResponse
          response = HttpResponse(path, content_type=mime_type)
          # Set the HTTP header for sending to browser
          response['Content-Disposition'] = "attachment; filename=%s" % filename
          # Return the response value
          return response

def download_report_paid(request):
          from django.conf import settings
          r = result.objects.latest('id') 
          filename = r.pdf_paid
          filepath =  str(settings.BASE_DIR) + "/survery_app/PDF/" + str(filename)

          path = open(filepath, 'rb')
          # Set the mime type
          mime_type, _ = mimetypes.guess_type(filepath)
          # Set the return value of the HttpResponse
          response = HttpResponse(path, content_type=mime_type)
          # Set the HTTP header for sending to browser
          response['Content-Disposition'] = "attachment; filename=%s" % filename
          # Return the response value
          return response


def paypal(request):
    return render(request, "paypal.html")


def paypal_success(request):
  r = result.objects.latest('id') 

  x = report_purchase_successful(
          four_letter_code = r.four_letter_code,
          user_name = r.user_name ,
          user_email = r.user_email,
          user_phone = r.user_phone,
          date_and_time_of_purchase = datetime.datetime.now()
          )
  x.save()


  return render(request, "paypal_success.html")

def c(request):
    return redirect('coupon')

def coupon(request):
  from survery_app.models import coupon
  from datetime import date

  if request.method == 'GET':
        return render(request, 'coupon.html')

  if request.method == 'POST':  

    if request.POST.get("coupon"):
      user_input_coupon = request.POST.get("coupon")

      all_coupon_codes = coupon.objects.all()
      for x in all_coupon_codes:
            print(x.code)

      for c in all_coupon_codes:
        print(c.code)
        if (c.code) == user_input_coupon:
              
              print("the code is : ")
              print(user_input_coupon)
              print()
              
              #expired TODO
              print("the expire date is : ")
              print(c.expire_date)
              print()
              print("the day today is ")
              print(date.today())

              if date.today() > c.expire_date:
                  c.attempts_after_expiry = c.attempts_after_expiry + 1
                  c.save()
                  if c.usage_limit < 0:
                    c.attempts_after_limit = c.attempts_after_limit + 1
                    c.save()
                  context = {
                        "message" : "coupon is expired, please use another coupon or skip",
                      }
                  return render(request, 'coupon.html' , context)

              # limit check
              if c.usage_limit < 0:
                 print("limit has been reached")
                 c.attempts_after_limit = c.attempts_after_limit + 1
                 c.save()
                 print(c.attempts_after_limit)
                 context = {
                  "message" : "coupon limit has been reached, please use another coupon or skip",
                }
                 return render(request, 'coupon.html' , context)

              # valid

              c.usage_limit = c.usage_limit - 1
              c.save()
              m = "your coupon " + user_input_coupon +  " is valid and has a worth of " + c.value 
              price = round(9.99 - float(c.value) , 2)

              context = {
                "message" : m,
                "price" : price,
              }
              return render(request, 'paypal.html' , context)

    
    context = {
                "message" : "coupon is NOT valid , please re try",
              }
    return render(request, 'coupon.html' , context)
        

def no_coupon(request):
  
  price = 9.99
  context = {
                "message" : " you did not use a coupon ",
                "price" : price,
              }
  return render(request, 'paypal.html' , context)