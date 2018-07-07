from django.db import models

# Create your models here.

std_choice = (
("1", "First Std"),
("2", "Second Std"),
)

diff_choice = (
(1,"Easy"),
(2,"Mid"),
(3,"Tough"),
)

mark_choice = (
(1,"One"),
(2,"Two"),
(3,"Three"),
)

sub_choice = (
("E","Englist"),
("T","Tamil"),
("M","Maths"),
)

type_choice = (
('1',"Choose the best answer"),
('2',"Choose multiple"),
('3',"True or False"),
('4',"Fill in the blanks"),
('5',"Spelling Check")
)

board_choice = (
("CBSE","CBSE"),
)

class QuestionBank(models.Model):
    standard = models.CharField(max_length=10,choices=std_choice)
    subject = models.CharField(max_length=10,choices=sub_choice)
    difficulty = models.PositiveIntegerField(choices=diff_choice)
    marks = models.PositiveIntegerField(choices=mark_choice)
    lessonNum = models.PositiveIntegerField(default=1)
    Q_image = models.URLField(max_length=1000, blank=True)
    QuestionType = models.CharField(max_length=1,default=1,choices=type_choice)
    Question = models.CharField(max_length=1000)
    answer_1 = models.CharField(max_length=200,blank=True)
    answer_1_ind = models.BooleanField(default=False)
    answer_2 = models.CharField(max_length=200,blank=True)
    answer_2_ind = models.BooleanField(default=False)
    answer_3 = models.CharField(max_length=200,blank=True)
    answer_3_ind = models.BooleanField(default=False)
    answer_4 = models.CharField(max_length=200,blank=True)
    answer_4_ind = models.BooleanField(default=False)
    answer_5 = models.CharField(max_length=200,blank=True)
    answer_5_ind = models.BooleanField(default=False)
    answer_6 = models.CharField(max_length=200,blank=True)
    answer_6_ind = models.BooleanField(default=False)

    def __str__(self):
        return '%s | %s | %s' % (self.standard, self.subject, self.Question)

class Grouping(models.Model):
    board = models.CharField(max_length=10, choices=board_choice)
    standard = models.CharField(max_length=10,choices=std_choice)
    subject = models.CharField(max_length=10,choices=sub_choice)
    lessonNum = models.PositiveIntegerField(default=1)
    lessonName = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '%s | %s | %s | %s' % (self.board, self.standard, self.subject, self.lessonNum)
