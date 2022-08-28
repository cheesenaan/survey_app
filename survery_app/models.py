from django.db import models

# DELETE FROM survery_app_question; DELETE FROM SQLite_sequence WHERE name='survery_app_question';

class question(models.Model):
    id = models.AutoField(primary_key=True)
    group_مجموعة = models.CharField(max_length=256, choices=[('Affinity', 'Affinity'), ('Collection of Information' , 'Collection of Information'), ('Make decison', 'Make decison') , ('Time spending' , 'Time spending') ])
    rank_النقاط = models.BigIntegerField()

    question_english_سؤال_الانجليزي = models.CharField(max_length=500)
    question_arabic_سؤال_عربي = models.CharField(max_length=500)

    title_of_answer_choice_one_عنوان_الإجابة_الأول= models.CharField(max_length=500)
    asnwer_choice_one_english_الإجابة_الأولى_انجليزي = models.CharField(max_length=500)
    asnwer_choice_one_arabic_الإجابة_الأولى_عربى = models.CharField(max_length=500)

    title_of_answer_choice_two_عنوان_الإجابة_الثاني = models.CharField(max_length=500)
    asnwer_choice_two_english_الإجابة_الثاني_انجليزي = models.CharField(max_length=500)
    asnwer_choice_two_arabic_الإجابة_الثاني_عربى = models.CharField(max_length=500)


class tally(models.Model):
    Affinity_choice1 = models.BigIntegerField()
    Affinity_choice2 = models.BigIntegerField()
    Collection_of_Information_choice1 = models.BigIntegerField()
    Collection_of_Information_choice2 = models.BigIntegerField()
    Make_decison_choice1 = models.BigIntegerField()
    Make_decison_choice2 = models.BigIntegerField()
    Time_spending_choice1 = models.BigIntegerField()
    Time_spending_choice2 = models.BigIntegerField()


