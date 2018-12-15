from django.conf.urls import url
from django.urls import path
from . import views

from quizapi.api.views import (

    QuestionBankListAPIView,
    QuestionBankListIdAPIView,
    QuestionBankDetailAPIView,
    QuestionBankDeleteAPIView,
    QuestionBankUpdateAPIView,
    QuestionBankCreateAPIView,

    PMPQuestionBankListAPIView,
    PMPQuestionBankDetailAPIView,
    PMPQuestionBankDeleteAPIView,
    PMPQuestionBankUpdateAPIView,
    PMPQuestionBankCreateAPIView,


    UserDetailsListAPIView,
    UserDetailsDetailAPIView,
    UserDetailsDeleteAPIView,
    UserDetailsUpdateAPIView,
    UserDetailsCreateAPIView,

    UserQuizListAPIView,
    UserQuizDetailAPIView,
    UserQuizDeleteAPIView,
    UserQuizUpdateAPIView,
    UserQuizCreateAPIView,

    GroupingListAPIView,
    GroupingDetailAPIView,
    GroupingDeleteAPIView,
    GroupingUpdateAPIView,
    GroupingCreateAPIView,
    GroupingBoardAPIView,
    GroupingStdAPIView,
    GroupingSubAPIView,
    GroupingLessonsAPIView,
    CreateUserAPIView,
    AuthUserAPIView,
)

urlpatterns = [

path('User/auth/',AuthUserAPIView.as_view(),name='AuthUserAPIView'),
path('User/create/',CreateUserAPIView.as_view(),name='CreateUserAPIView'),
path('QuestionList/',QuestionBankListAPIView.as_view(),name='QuestionBankListAPIView'),
path('QuestionList/create',QuestionBankCreateAPIView.as_view(),name='QuestionBankCreateAPIView'),
path('QuestionList/<int:pk>',QuestionBankDetailAPIView.as_view(),name='QuestionBankDetailAPIView'),
path('QuestionList/edit/<int:pk>',QuestionBankUpdateAPIView.as_view(),name='QuestionBankUpdateAPIView'),
path('QuestionList/delete/<int:pk>',QuestionBankDeleteAPIView.as_view(),name='QuestionBankDeleteAPIView'),

path('PMPQuestionList/',PMPQuestionBankListAPIView.as_view(),name='PMPQuestionBankListAPIView'),
path('PMPQuestionList/create',PMPQuestionBankCreateAPIView.as_view(),name='PMPQuestionBankCreateAPIView'),
path('PMPQuestionList/<int:pk>',PMPQuestionBankDetailAPIView.as_view(),name='PMPQuestionBankDetailAPIView'),
path('PMPQuestionList/edit/<int:pk>',PMPQuestionBankUpdateAPIView.as_view(),name='PMPQuestionBankUpdateAPIView'),
path('PMPQuestionList/delete/<int:pk>',PMPQuestionBankDeleteAPIView.as_view(),name='PMPQuestionBankDeleteAPIView'),

path('UserDetails/',UserDetailsListAPIView.as_view(),name='UserDetailsListAPIView'),
path('UserDetails/create',UserDetailsCreateAPIView.as_view(),name='UserDetailsCreateAPIView'),
path('UserDetails/<int:pk>',UserDetailsDetailAPIView.as_view(),name='UserDetailsDetailAPIView'),
path('UserDetails/edit/<int:pk>',UserDetailsUpdateAPIView.as_view(),name='UserDetailsUpdateAPIView'),

path('UserQuiz/',UserQuizListAPIView.as_view(),name='UserQuizListAPIView'),
path('UserQuiz/create',UserQuizCreateAPIView.as_view(),name='UserQuizCreateAPIView'),
path('UserQuiz/<int:pk>',UserQuizDetailAPIView.as_view(),name='UserQuizDetailAPIView'),
path('UserQuiz/edit/<int:pk>',UserQuizUpdateAPIView.as_view(),name='UserQuizUpdateAPIView'),

path('Grouping/',GroupingListAPIView.as_view(),name='GroupingListAPIView'),
path('Grouping/board/',GroupingBoardAPIView.as_view(),name='GroupingBoardAPIView'),
path('Grouping/std/',GroupingStdAPIView.as_view(),name='GroupingStdAPIView'),
path('Grouping/sub/',GroupingSubAPIView.as_view(),name='GroupingSubAPIView'),
path('Grouping/lessons/',GroupingLessonsAPIView.as_view(),name='GroupingLessonsAPIView'),
path('Grouping/create/',GroupingCreateAPIView.as_view(),name='GroupingCreateAPIView'),
path('Grouping/<int:pk>/',GroupingDetailAPIView.as_view(),name='GroupingDetailAPIView'),
path('Grouping/edit/<int:pk>/',GroupingUpdateAPIView.as_view(),name='GroupingUpdateAPIView'),
path('Grouping/delete/<int:pk>/',GroupingDeleteAPIView.as_view(),name='GroupingDeleteAPIView'),




]
