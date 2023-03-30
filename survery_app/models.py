from email.policy import default
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

# <script src="https://www.paypal.com/sdk/js?client-id=AVg80mzhIITpV4AntbRZIulWJ4YiJIIWhXMcNjl3WeLKD8VBrOs_S-wP9Yi-CHlEqJ2PKZyDCjTEv7A-&currency=USD&intent=capture&enable-funding=venmo" data-sdk-integration-source="integrationbuilder"></script>


class result(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=500)

    affinity_1 = models.BigIntegerField()
    affinity_2 = models.BigIntegerField()
    affinity_result= models.CharField(max_length=500)

    collection_1 = models.BigIntegerField()
    collection_2 = models.BigIntegerField()
    collection_result = models.CharField(max_length=500)

    make_1 = models.BigIntegerField()
    make_2 = models.BigIntegerField()
    make_result = models.CharField(max_length=500)

    time_1 = models.BigIntegerField()
    time_2 = models.BigIntegerField()
    time_result = models.CharField(max_length=500)

    pdf_answer_case = models.BigIntegerField()
    user_name = models.CharField(max_length=500)
    user_email = models.CharField(max_length=500)
    user_phone = models.CharField(max_length=500)

    four_letter_code  = models.CharField(max_length=500)
    pdf_free = models.CharField(max_length=500)
    pdf_paid = models.CharField(max_length=500)

    link = models.CharField(max_length=500)

    date_and_time_completed = models.CharField(max_length=500)


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


# there will always be only one row in this model. they are just counters
class group_choice_change(models.Model):
    id = models.AutoField(primary_key=True)

    affinity_Extrovert_to_Introvert = models.BigIntegerField(default=0)
    affinity_Introvert_to_Extrovert = models.BigIntegerField(default=0)

    collection_Sensing_to_Intuition = models.BigIntegerField(default=0)
    collection_Intuition_to_Sensing = models.BigIntegerField(default=0)

    make_Thinking_to_Feeling = models.BigIntegerField(default=0)
    make_Feeling_to_Thinking = models.BigIntegerField(default=0)

    time_Judging_to_Perceiving = models.BigIntegerField(default=0)
    time_Perceiving_to_Judging = models.BigIntegerField(default=0)

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
    

# /first_name/last_name/paid_report_download #
# that would be the link #

class report_purchase_successful(models.Model):
    id_result_reference = models.BigIntegerField()
    four_letter_code  = models.CharField(max_length=500)
    user_name = models.CharField(max_length=500)
    user_email = models.CharField(max_length=500)
    user_phone = models.CharField(max_length=500)
    date_and_time_of_purchase = models.DateTimeField()



class coupon(models.Model):
    coupon_type = models.CharField(max_length=256, choices=[('name system', 'name system'), ('random number' , 'random number'), ('custom name', 'custom name')])
    code = models.CharField(max_length=500)
    value = models.FloatField(default=1)
    expire_date = models.DateField()
    usage_limit = models.BigIntegerField()
    attempts_after_limit = models.BigIntegerField(default=0) # see who is trying to use the coupon after the limit has been reached
    attempts_after_expiry = models.BigIntegerField(default=0) # see who is trying to use the coupon after it has been expired



# model of who downloaded
class free_download(models.Model):
    result_id = models.BigIntegerField(default=0)
    user_name = models.CharField(max_length=500)
    user_email = models.CharField(max_length=500)
    link = models.CharField(max_length=500)


# who downloaded
class paid_download(models.Model):
    result_id = models.BigIntegerField()
    user_name = models.CharField(max_length=500)
    user_email = models.CharField(max_length=500)
    link = models.CharField(max_length=500)


class marketers(models.Model):
    member_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    user_email = models.CharField(max_length=500)
    paypal_email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

    number_of_visits = models.BigIntegerField(default=0)
    number_of_free_downloads = models.BigIntegerField(default=0)
    number_of_receipt_downloads = models.BigIntegerField(default=0)
    number_of_payments = models.BigIntegerField(default=0)
    number_of_paid_downloads = models.BigIntegerField(default=0)

    amount_earned = models.FloatField(default=0)




