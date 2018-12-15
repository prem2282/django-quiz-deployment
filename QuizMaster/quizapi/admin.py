from django.contrib import admin
from quizapi.models import QuestionBank,Grouping,UserDetails,UserQuiz,PMPQuestionBank
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# pip install django-import-export

@admin.register(QuestionBank)
class QuestionAdmin(ImportExportModelAdmin):
    list_display = ('id','standard','subject','difficulty','marks','Question','answer_1','answer_2','answer_3','answer_4','answer_5','answer_6','answer_1_ind','answer_2_ind','answer_3_ind','answer_4_ind','answer_5_ind','answer_6_ind')
    list_editable = ('standard','subject','difficulty','marks','Question','answer_1','answer_2','answer_3','answer_4','answer_5','answer_6','answer_1_ind','answer_2_ind','answer_3_ind','answer_4_ind','answer_5_ind','answer_6_ind')

@admin.register(PMPQuestionBank)
class PMPQuestionAdmin(ImportExportModelAdmin):
    list_display = ('id','standard','subject','difficulty','marks','Question','answer_1','answer_2','answer_3','answer_4','answer_5','answer_6','answer_1_ind','answer_2_ind','answer_3_ind','answer_4_ind','answer_5_ind','answer_6_ind')
    list_editable = ('standard','subject','difficulty','marks','Question','answer_1','answer_2','answer_3','answer_4','answer_5','answer_6','answer_1_ind','answer_2_ind','answer_3_ind','answer_4_ind','answer_5_ind','answer_6_ind')

@admin.register(Grouping)
class GroupingAdmin(ImportExportModelAdmin):
    list_display = ('id','board','standard','subject','lessonNum','lessonName')
    list_editable = ('board','standard','subject','lessonNum','lessonName')

@admin.register(UserDetails)
class UserDetailsAdmin(ImportExportModelAdmin):
    list_display = ('id','userId','userName','userEmail','imageUrl','registeredDate','loginTime')
    list_editable = ('userId','userName','userEmail','imageUrl','registeredDate','loginTime')

@admin.register(UserQuiz)
class UserQuizAdmin(ImportExportModelAdmin):
    list_display = ('id','userId','groupId','questionSet','answerSet','variableSet','selectedAnsIndex','score','updatedTime','quizStatus')
    list_editable = ('userId','groupId','questionSet','answerSet','variableSet','selectedAnsIndex','score','updatedTime','quizStatus')
