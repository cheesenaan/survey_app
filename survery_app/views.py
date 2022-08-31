from contextlib import _RedirectStream
import re
from xml.etree.ElementTree import tostring
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from fpdf import FPDF


pdf_answer_case = 0
file = None

# Create your views here.
def home(request):
  return render(request, "home.html")

def RIASEC_survey_arabic(request):
      return render(request, "RIASEC_survey_arabic.html")



def survey_arabic(request):
    if request.method == 'POST':
        print(request.POST)
        questions=question.objects.all()

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

            print("this is the request : ")
            print(request.POST.get(q.question_arabic_سؤال_عربي))
            print(affinity_1_heading)
            print(affinity_2_heading)
            print(collection_1_heading)
            print(collection_2_heading)
            print(make_1_heading)
            print(make_2_heading)
            print(time_1_heading)
            print(time_2_heading)
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

        }


        return render(request,'after_survey_arabic.html',context)


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
  

  