from django.db import models
from django.contrib.auth.models import User
class Exams(models.Model):
    subject_name = models.CharField(max_length=300)
    total_questions = models.FloatField()
    total_mark = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject_name
class Questions(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Exams, on_delete=models.CASCADE)
    question = models.CharField(max_length=3000)
    marks = models.FloatField()
    choice1 = models.CharField(max_length=3000)
    choice2 = models.CharField(max_length=3000)
    choice3 = models.CharField(max_length=3000)
    choice4 = models.CharField(max_length=3000)
    choices = [
        ('A', 'choice1'),
        ('B', "choice2"),
        ("C", "choice3"),
        ("D", "choice4"),
         ]
    answer = models.CharField(choices=choices, max_length=3000)
class Result(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Exams, on_delete=models.CASCADE)
    result = models.FloatField()
    def __str__(self):
        return self.result