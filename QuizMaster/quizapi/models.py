from django.db import models

# Create your models here.

PMP_std_choice = (
("I","Initiating"),
("P","Planning"),
("E","Executing"),
("M","Monitoring and Control"),
("C","Closing"),
("ET","Ethics"),
("G","General"),

)

std_choice = (
("1", "1st Std"),
("2", "2nd Std"),
("3", "3rd Std"),
("4", "4th Std"),
("5", "5th Std"),
("6", "6th Std"),
("7", "7th Std"),
("8", "8th Std"),
("9", "9th Std"),
("10", "10th Std"),
("11", "11th Std"),
("12", "12th Std"),
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
(4,"Four"),
(5,"Five"),
)

PMP_sub_choice = (
("I","Integration"),
("S","Scope"),
("T","Time"),
("C","Cost"),
("Q","Quality"),
("H","Human Resources"),
("CM","Communication"),
("R","Risk"),
("P","Procurement"),
("ET","Ethics"),
("G","Generals"),
)

sub_choice = (
("E","Englist"),
("T","Tamil"),
("M","Maths"),
("GK","GK"),
("SS","Social Science"),
("S","Science"),
("ES","Environmental Science"),
("CS","Computer Science"),
("H","Hindi"),
)

type_choice = (
('1',"Choose the best answer"),
('2',"Choose multiple"),
('3',"True or False"),
('4',"Fill in the blanks"),
('5',"Math")
)

board_choice = (
("CBSE","CBSE"),
)

class Grouping(models.Model):
    category = models.CharField(max_length=20,default='Academics')
    board = models.CharField(max_length=20)
    standard = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    lessonNum = models.PositiveIntegerField(default=1)
    lessonName = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '%s | %s | %s | %s | %s' % (self.category, self.board, self.standard, self.subject, self.lessonNum)

class QuestionBank(models.Model):
    category = models.CharField(max_length=20,default='Academics')
    board = models.CharField(max_length=20,default='CBSE')
    standard = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
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
        return '%s | %s | %s | %s | %s' % (self.category, self.board, self.standard, self.subject, self.Question)

class PMPQuestionBank(models.Model):
    standard = models.CharField(max_length=10,choices=PMP_std_choice)
    subject = models.CharField(max_length=10,choices=PMP_sub_choice)
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

class MusicBank(models.Model):
    title = models.CharField(max_length=50)
    movie = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=15, blank=True)
    composer = models.CharField(max_length=15, blank=True)
    imageUrl = models.URLField(max_length=1000, blank=True)
    notes = models.CharField(max_length=10000)
    lyrics = models.CharField(max_length=10000, blank=True)
    localLyrics = models.CharField(max_length=10000, blank=True)
    noteSplit = models.CharField(max_length=500, blank=True)
    sectionSplit = models.CharField(max_length=500, blank=True)
    scale = models.CharField(max_length=20, blank=True)
    raga = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '%s | %s | %s' % (self.title, self.movie, self.language)


class CodeBank(models.Model):
    subject = models.CharField(max_length=30)
    level = models.PositiveIntegerField(default=1)
    section = models.CharField(max_length=30)
    seq_num = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=50)
    contributor = models.CharField(max_length=100,blank=True)
    description_1 = models.CharField(max_length=1000,blank=True)
    description_2 = models.CharField(max_length=1000,blank=True)
    description_3 = models.CharField(max_length=1000,blank=True)
    code_1 = models.CharField(max_length=2000,blank=True)
    code_1_type = models.CharField(max_length=10,blank=True)
    code_2 = models.CharField(max_length=2000,blank=True)
    code_2_type = models.CharField(max_length=10,blank=True)  
    code_3 = models.CharField(max_length=2000,blank=True)
    code_3_type = models.CharField(max_length=10,blank=True)
    code_4 = models.CharField(max_length=2000,blank=True)
    code_4_type = models.CharField(max_length=10,blank=True)    
    def __str__(self):
        return '%s | %s | %s | %s | %s' % (self.subject, self.level, self.section, self.seq_num, self.title)

class UserDetails(models.Model):
    userId = models.CharField(max_length=50,unique=True)
    userName = models.CharField(max_length=50,blank=True)
    userEmail = models.CharField(max_length=50,blank=True)
    imageUrl = models.CharField(max_length=500,blank=True)
    registeredDate = models.CharField(max_length=50,blank=True)
    loginTime = models.CharField(max_length=50,blank=True)


    def __str__(self):
        return '%s | %s  ' % (self.userId, self.userName)

class UserPackage(models.Model):
    userId = models.CharField(max_length=50,blank=True)
    paymentGateway = models.CharField(max_length=20)
    packageId = models.CharField(max_length=20,blank=True)
    paymentId = models.CharField(max_length=200,blank=True)
    paymentId2 = models.CharField(max_length=200,blank=True)
    requestId = models.CharField(max_length=200,blank=True)
    paymentDate = models.CharField(max_length=50,blank=True)
    startDate = models.CharField(max_length=50,blank=True)
    endDate = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return '%s | %s  ' % (self.userId, self.packageId)

class UserQuiz(models.Model):
    userId = models.CharField(max_length=50,blank=True)
    groupId =  models.CharField(max_length=50,blank=True)
    customId = models.CharField(max_length=50,blank=True)
    questionSet = models.CharField(max_length=500,blank=True)
    answerSet = models.CharField(max_length=500,blank=True)
    variableSet = models.CharField(max_length=500,blank=True)
    selectedAnsIndex = models.CharField(max_length=500,blank=True)
    score = models.PositiveIntegerField(default=0)
    updatedTime = models.CharField(max_length=50,blank=True)
    quizStatus = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return '%s | %s ' % (self.userId, self.groupId)

class Constants(models.Model):
    varName = models.CharField(max_length=40,blank=True)
    varSeqNo = models.PositiveIntegerField(default=0)
    varValue = models.CharField(max_length=500,blank=True)
