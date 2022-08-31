from django.db import models

# DELETE FROM survery_app_question; DELETE FROM SQLite_sequence WHERE name='survery_app_question';

# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py runserver





# class question(models.Model):
#     id = models.AutoField(primary_key=True)
#     group_مجموعة = models.CharField(max_length=256, choices=[('Affinity', 'Affinity'), ('Collection of Information' , 'Collection of information'), ('Make decison', 'Make decison') , ('Time spending' , 'Time spending') ])
#     rank_النقاط = models.BigIntegerField()

#     question_english_سؤال_الانجليزي = models.CharField(max_length=500)
#     question_arabic_سؤال_عربي = models.CharField(max_length=500)

#     title_of_answer_choice_one_عنوان_الإجابة_الأول= models.CharField(max_length=256, choices=[('Extrovert', 'Extrovert'), ('Sensing' , 'Sensing'), ('Thinking', 'Thinking') , ('Judging' , 'Judging') ])

#     asnwer_choice_one_english_الإجابة_الأولى_انجليزي = models.CharField(max_length=500)
#     asnwer_choice_one_arabic_الإجابة_الأولى_عربى = models.CharField(max_length=500)

#     title_of_answer_choice_two_عنوان_الإجابة_الثاني = models.CharField(max_length=256, choices=[('Introvert', 'Introvert'), ('Intuition' , 'Intuition'), ('Feeling', 'Feeling') , ('Perceiving' , 'Perceiving') ])
#     asnwer_choice_two_english_الإجابة_الثاني_انجليزي = models.CharField(max_length=500)
#     asnwer_choice_two_arabic_الإجابة_الثاني_عربى = models.CharField(max_length=500)

class question(models.Model):
    id = models.AutoField(primary_key=True)
    group_مجموعة = models.CharField(max_length=256, choices=[('Affinity', 'Affinity'), ('Collection of information' , 'Collection of information'), ('Make decision', 'Make decision') , ('Time spending' , 'Time spending') ])
    rank_النقاط = models.BigIntegerField()

    question_english_سؤال_الانجليزي = models.CharField(max_length=500)
    question_arabic_سؤال_عربي = models.CharField(max_length=500)

    title_of_answer_choice_one_عنوان_الإجابة_الأول= models.CharField(max_length=256, choices=[('Extrovert', 'Extrovert'), ('Sensing' , 'Sensing'), ('Thinking', 'Thinking') , ('Judging' , 'Judging') ])

    asnwer_choice_one_english_الإجابة_الأولى_انجليزي = models.CharField(max_length=500)
    asnwer_choice_one_arabic_الإجابة_الأولى_عربى = models.CharField(max_length=500)

    title_of_answer_choice_two_عنوان_الإجابة_الثاني = models.CharField(max_length=256, choices=[('Introvert', 'Introvert'), ('Intuition' , 'Intuition'), ('Feeling', 'Feeling') , ('Perceiving' , 'Perceiving') ])
    asnwer_choice_two_english_الإجابة_الثاني_انجليزي = models.CharField(max_length=500)
    asnwer_choice_two_arabic_الإجابة_الثاني_عربى = models.CharField(max_length=500)


class RIASEC(models.Model):
    id = models.AutoField(primary_key=True)

    group_مجموعة = models.CharField(max_length=256, 

    choices=[('Realistic', 'Realistic'),
     ('Investigative' ,'Investigative'), 
    ('Artistic', 'Artistic') ,
    ('Social' , 'Social') ,
    ('Enterprising' , 'Enterprising') ,
    ('Conventional' , 'Conventional')])

    rank_النقاط = models.BigIntegerField()

    question_english_سؤال_الانجليزي = models.CharField(max_length=500)
    question_arabic_سؤال_عربي = models.CharField(max_length=500)


    asnwer_choice_one_english_الإجابة_الأولى_انجليزي = models.CharField(max_length=500)
    asnwer_choice_one_arabic_الإجابة_الأولى_عربى = models.CharField(max_length=500)

    asnwer_choice_two_english_الإجابة_الثاني_انجليزي = models.CharField(max_length=500)
    asnwer_choice_two_arabic_الإجابة_الثاني_عربى = models.CharField(max_length=500)

    answer_choice_three_english = models.CharField(max_length=500)
    answer_choice_three_arabic = models.CharField(max_length=500)

    answer_choice_four_english = models.CharField(max_length=500)
    answer_choice_four_arabic = models.CharField(max_length=500)

    answer_choice_five_english = models.CharField(max_length=500)
    answer_choice_five_arabic = models.CharField(max_length=500)
    


