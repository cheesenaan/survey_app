import os
import sys
import csv

import  os
os.environ.setdefault("DJANGO_SETTINGS_MODULE" , "survery_project.settings")

# python3 manage.py flush
# python3 load_questions.py
import django
django.setup()

sys.path.append("/Users/cheesenaan/Documents/qatar work/project/env_site/survery_project/survery_app")
from survery_app.models import question



with open('backend.csv') as file:
    question.objects.all().delete()
    reader = csv.reader(file)
    next(reader)  # Advance past the header

    for row in reader:
        group = row[0]
        question_arabic = row[1]
        question_english = row[2]
        ESTJ_Arabic = row[3]
        ESTJ_English = row[4]
        INFP_Arabic = row[5]
        INFP_English = row[6]
        Rank = row[7]
        title1 = row[8]
        title2 = row[9]

        q = question(
            group_مجموعة = group,
            rank_النقاط = Rank,

            question_english_سؤال_الانجليزي = question_english,
            question_arabic_سؤال_عربي = question_arabic,

            title_of_answer_choice_one_عنوان_الإجابة_الأول= title1,

            asnwer_choice_one_english_الإجابة_الأولى_انجليزي = ESTJ_English,
            asnwer_choice_one_arabic_الإجابة_الأولى_عربى = ESTJ_Arabic,

            title_of_answer_choice_two_عنوان_الإجابة_الثاني = title2,
            asnwer_choice_two_english_الإجابة_الثاني_انجليزي = INFP_English,
            asnwer_choice_two_arabic_الإجابة_الثاني_عربى = INFP_Arabic
        )
        q.save()
