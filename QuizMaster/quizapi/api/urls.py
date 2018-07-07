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
