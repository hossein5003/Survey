from django.db import models


class Survey(models.Model):
    Survey_Id=models.CharField(max_length=15)
    Survey_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Survey_Name


class Question(models.Model):
    Question_Id=models.IntegerField(unique=True)
    survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text


class SurveyAnswer(models.Model):
    Survey_Id=models.ForeignKey(Survey)
    Question_Id = models.ForeignKey(Question)
    Question_Answer=models.CharField(max_length=255)


class Choice(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.question.text}:{self.text}"


class Submission(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
    participant_email = models.EmailField(max_length=255)
    answer = models.ManyToManyField(Choice)
    status = models.CharField(max_length=255)
