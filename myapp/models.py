from django.db import models

# Create your models here.


class Article(models.Model):
    date = models.DateField(auto_now_add=True)
    print(date)
    heading = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="article_images")

class Test(models.Model):
    subject = models.CharField(max_length=255)
    date = models.DateField()
    # Many-to-Many relationship with questions
    questions = models.ManyToManyField('self', symmetrical=False, through='Question', blank=False)

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    description = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    # Use a CharField to store the correct option (A, B, C, D)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    answer_description = models.TextField()

