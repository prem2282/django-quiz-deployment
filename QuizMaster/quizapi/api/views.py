from django.db.models import Q
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import (
CreateAPIView,
ListAPIView,
RetrieveAPIView,
RetrieveUpdateAPIView,
UpdateAPIView,
DestroyAPIView,
)

from quizapi.models import QuestionBank, Grouping
from django.contrib.auth import get_user_model
User = get_user_model()

from .serializers import (

QuestionBankSerializer,
QuestionBankIdSerializer,
QuestionBankCreateSerializer,
GroupingSerializer,
GroupingBoardSerializer,
GroupingStdSerializer,
GroupingSubSerializer,
GroupingLessonsSerializer,
GroupingCreateSerializer,
UserSerializer,

)


class AuthUserAPIView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)

class CreateUserAPIView(CreateAPIView):

    model = User();
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

class QuestionBankCreateAPIView(CreateAPIView):
    quesyset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer

class QuestionBankListIdAPIView(ListAPIView):
    quesyset = QuestionBank.objects.all()
    serializer_class = QuestionBankIdSerializer


class QuestionBankListAPIView(ListAPIView):
    quesyset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = QuestionBank.objects.all()
        q1 = self.request.GET.get("sub")
        q2 = self.request.GET.get("std")
        q3 = self.request.GET.get("lessons")

        if (q1 and q2 and q3):
            quesryset_list = queryset_list.filter(
            Q(subject_iexact=q1)&
            Q(standard_iexact=q2)&
            Q(lessonNum_iexact=q3)
            ).distinct().order_by('?')[:15]
        if (q1 and q2):
            quesryset_list = queryset_list.filter(
            Q(subject_iexact=q1)&
            Q(standard_iexact=q2)
            ).distinct().order_by('?')[:15]
        elif (q2 and q3):
            quesryset_list = queryset_list.filter(
            Q(standard_iexact=q2)&
            Q(lessonNum_iexact=q3)
            ).distinct().order_by('?')[:15]
        if (q1):
            quesryset_list = queryset_list.filter(
            Q(subject_iexact=q1)
            ).distinct().order_by('?')[:15]

        return queryset_list

class QuestionBankDetailAPIView(RetrieveAPIView):
    quesyset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer

class QuestionBankUpdateAPIView(RetrieveUpdateAPIView):
    quesyset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer


class QuestionBankDeleteAPIView(DestroyAPIView):
    quesyset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer

class GroupingListAPIView(ListAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingSerializer

class GroupingBoardAPIView(ListAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingBoardSerializer
    def get_queryset(self,*args,**kwargs):
        queryset_list = Grouping.objects.values("board").distinct()
        return queryset_list

class GroupingStdAPIView(ListAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingStdSerializer
    def get_queryset(self,*args,**kwargs):
        queryset_list = Grouping.objects.all()
        q1 = self.request.GET.get("board")
        if (q1):
            queryset_list = queryset_list.filter(
            Q(board_iexact=q1)
            ).values("standard").distinct().order_by("standard")
        return queryset_list

class GroupingSubAPIView(ListAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingSubSerializer
    def get_queryset(self,*args,**kwargs):
        queryset_list = Grouping.objects.all()
        q1 = self.request.GET.get("board")
        q2 = self.request.GET.get("std")
        if (q1 and q2):
            queryset_list = queryset_list.filter(
            Q(board_iexact=q1)&
            Q(standard_iexact=q2)
            ).values("subject").distinct()
        return queryset_list

class GroupingLessonsAPIView(ListAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingLessonsSerializer
    def get_queryset(self,*args,**kwargs):
        queryset_list = Grouping.objects.all()
        q1 = self.request.GET.get("board")
        q2 = self.request.GET.get("std")
        q3 = self.request.GET.get("sub")
        if (q1 and q2 and q3):
            queryset_list = queryset_list.filter(
            Q(board_iexact=q1)&
            Q(standard_iexact=q2)&
            Q(subject_iexact=q3)
            ).values("lessonNum","lessonName").distinct().order_by("lessonNum")
        return queryset_list

class GroupingDetailAPIView(RetrieveAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingSerializer

class GroupingCreateAPIView(CreateAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingCreateSerializer

class GroupingUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingSerializer


class GroupingDeleteAPIView(DestroyAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingSerializer
