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

from quizapi.models import QuestionBank, Grouping, PMPQuestionBank, MusicBank, CodeBank, UserQuiz, UserDetails, UserPackage, Constants
from django.contrib.auth import get_user_model
User = get_user_model()

from .serializers import (

QuestionBankSerializer,
QuestionBankIdSerializer,
QuestionBankCreateSerializer,
PMPQuestionBankSerializer,
PMPQuestionBankIdSerializer,
PMPQuestionBankCreateSerializer,
MusicBankSerializer,
MusicBankIdSerializer,
MusicBankCreateSerializer,
CodeBankSerializer,
CodeBankIdSerializer,
CodeBankCreateSerializer,
GroupingSerializer,
GroupingBoardSerializer,
GroupingStdSerializer,
GroupingSubSerializer,
GroupingLessonsSerializer,
GroupingCreateSerializer,
UserSerializer,
UserDetailsSerializer,
UserQuizSerializer,
UserPackageSerializer,
ConstantsSerializer,
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

class UserDetailsCreateAPIView(CreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class ConstantsCreateAPIView(CreateAPIView):
    queryset = Constants.objects.all()
    serializer_class = ConstantsSerializer

class UserPackageCreateAPIView(CreateAPIView):
    queryset = UserPackage.objects.all()
    serializer_class = UserPackageSerializer

class UserQuizCreateAPIView(CreateAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer

class PMPQuestionBankCreateAPIView(CreateAPIView):
    queryset = PMPQuestionBank.objects.all()
    serializer_class = PMPQuestionBankSerializer


class PMPQuestionBankListAPIView(ListAPIView):
    queryset = PMPQuestionBank.objects.all()
    serializer_class = PMPQuestionBankSerializer


class MusicBankCreateAPIView(CreateAPIView):
    queryset = MusicBank.objects.all()
    serializer_class = MusicBankSerializer


class MusicBankListAPIView(ListAPIView):
    queryset = MusicBank.objects.all()
    serializer_class = MusicBankSerializer

class CodeBankCreateAPIView(CreateAPIView):
    queryset = CodeBank.objects.all()
    serializer_class = CodeBankSerializer


class CodeBankListAPIView(ListAPIView):
    queryset = CodeBank.objects.all().values("id","subject","level","section","seq_num",'title').distinct().order_by("seq_num")
    serializer_class = CodeBankSerializer

class CodeBankListMenuAPIView(ListAPIView):
    queryset = CodeBank.objects.all()
    serializer_class = CodeBankSerializer

class QuestionBankCreateAPIView(CreateAPIView):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer

class QuestionBankListIdAPIView(ListAPIView):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankIdSerializer


class QuestionBankListAPIView(ListAPIView):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = QuestionBank.objects.all()
        queryset_final = ''
        q6 =''
        q6a = ''
        q1 = self.request.GET.get("category")
        q2 = self.request.GET.get("board")
        q3 = self.request.GET.get("standard")
        q4 = self.request.GET.get("subject")
        q5a = self.request.GET.get("lessonNum")
        if q5a is not None:
            q5 = list(q5a.split("-"))
        q6a = self.request.GET.get("questionSet")
        if q6a is not None:
            q6 = list(q6a.split("-"))
        if (q1 and q2 and q3 and q4 and q5):
            queryset_final = queryset_list.filter(
            Q(category__iexact=q1)&
            Q(board__iexact=q2)&
            Q(standard__iexact=q3)&
            Q(subject__iexact=q4)&
            Q(lessonNum__in=q5)
            ).distinct()
        elif (q6):
            queryset_final = queryset_list.filter(
            Q(id__in=q6)
            ).distinct()
        elif (q1):
            queryset_final = queryset_list.filter(
            Q(category__iexact=q1)
            ).distinct()
        return queryset_final

class QuestionBankDetailAPIView(RetrieveAPIView):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer

class PMPQuestionBankDetailAPIView(RetrieveAPIView):
    queryset = PMPQuestionBank.objects.all()
    serializer_class = PMPQuestionBankSerializer

class MusicBankDetailAPIView(RetrieveAPIView):
    queryset = MusicBank.objects.all()
    serializer_class = MusicBankSerializer

class CodeBankDetailAPIView(RetrieveAPIView):
    queryset = CodeBank.objects.all()
    serializer_class = CodeBankSerializer

class UserDetailsDetailAPIView(RetrieveAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class ConstantsDetailAPIView(RetrieveAPIView):
    queryset = Constants.objects.all()
    serializer_class = ConstantsSerializer

class UserPackageDetailAPIView(RetrieveAPIView):
    queryset = UserPackage.objects.all()
    serializer_class = UserPackageSerializer

class UserQuizDetailAPIView(RetrieveAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer

class QuestionBankUpdateAPIView(RetrieveUpdateAPIView):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer

class PMPQuestionBankUpdateAPIView(RetrieveUpdateAPIView):
    queryset = PMPQuestionBank.objects.all()
    serializer_class = PMPQuestionBankSerializer

class MusicBankUpdateAPIView(RetrieveUpdateAPIView):
    queryset = MusicBank.objects.all()
    serializer_class = MusicBankSerializer    

class CodeBankUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CodeBank.objects.all()
    serializer_class = CodeBankSerializer    

class UserDetailsUpdateAPIView(RetrieveUpdateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class ConstantsUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Constants.objects.all()
    serializer_class = ConstantsSerializer

class UserPackageUpdateAPIView(RetrieveUpdateAPIView):
    queryset = UserPackage.objects.all()
    serializer_class = UserPackageSerializer

class UserQuizUpdateAPIView(RetrieveUpdateAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer


class QuestionBankDeleteAPIView(DestroyAPIView):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer

class PMPQuestionBankDeleteAPIView(DestroyAPIView):
    queryset = PMPQuestionBank.objects.all()
    serializer_class = PMPQuestionBankSerializer

class MusicBankDeleteAPIView(DestroyAPIView):
    queryset = MusicBank.objects.all()
    serializer_class = MusicBankSerializer

class CodeBankDeleteAPIView(DestroyAPIView):
    queryset = CodeBank.objects.all()
    serializer_class = CodeBankSerializer

class UserDetailsDeleteAPIView(DestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class ConstantsDeleteAPIView(DestroyAPIView):
    queryset = Constants.objects.all()
    serializer_class = ConstantsSerializer

class UserPackageDeleteAPIView(DestroyAPIView):
    queryset = UserPackage.objects.all()
    serializer_class = UserPackageSerializer

class UserQuizDeleteAPIView(DestroyAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer

class UserDetailsListAPIView(ListAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

    def get_queryset(self,*args,**kwargs):
        queryset_list = UserDetails.objects.all()
        q1 = self.request.GET.get("userId")
        if (q1):
            queryset_list = queryset_list.filter(
            Q(userId__iexact=q1)
            ).distinct()
        return queryset_list

class ConstantsListAPIView(ListAPIView):
    queryset = Constants.objects.all()
    serializer_class = ConstantsSerializer

    def get_queryset(self,*args,**kwargs):
        queryset_list = Constants.objects.all()
        q1 = self.request.GET.get("varName")
        if (q1):
            queryset_list = queryset_list.filter(
            Q(varName__iexact=q1)
            ).distinct()
        return queryset_list


class UserPackageListAPIView(ListAPIView):
    queryset = UserPackage.objects.all()
    serializer_class = UserPackageSerializer

    def get_queryset(self,*args,**kwargs):
        queryset_list = UserPackage.objects.all()
        q1 = self.request.GET.get("userId")
        if (q1):
            queryset_list = queryset_list.filter(
            Q(userId__iexact=q1)
            ).distinct()
        return queryset_list

class UserQuizListAPIView(ListAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer

    def get_queryset(self,*args,**kwargs):
        queryset_list = UserQuiz.objects.all()
        q1 = self.request.GET.get("userId")
        q2 = self.request.GET.get("groupId")
        q3 = self.request.GET.get("quizStatus")
        if (q1 and q2 and q3):
            queryset_list = queryset_list.filter(
            Q(userId__iexact=q1)&
            Q(groupId__iexact=q2)&
            Q(quizStatus__iexact=q3)
            ).distinct().order_by('-updatedTime')
        elif (q1):
            queryset_list = queryset_list.filter(
            Q(userId__iexact=q1)
            ).distinct().order_by('-updatedTime')
        return queryset_list


class GroupingListAPIView(ListAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingSerializer

class GroupingBoardAPIView(ListAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingBoardSerializer
    def get_queryset(self,*args,**kwargs):
        queryset_list = Grouping.objects.values("category","board","standard","subject").distinct()
        return queryset_list

class GroupingStdAPIView(ListAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingStdSerializer
    def get_queryset(self,*args,**kwargs):
        queryset_list = Grouping.objects.all()
        q0 = self.request.GET.get("category")
        q1 = self.request.GET.get("board")
        if (q1):
            queryset_list = queryset_list.filter(
            Q(category_iexact=q0)&
            Q(board_iexact=q1)
            ).values("standard","subject").distinct().order_by("standard")
        return queryset_list

class GroupingSubAPIView(ListAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingSubSerializer
    def get_queryset(self,*args,**kwargs):
        queryset_list = Grouping.objects.all()
        q0 = self.request.GET.get("category")
        q1 = self.request.GET.get("board")
        q2 = self.request.GET.get("std")
        if (q1 and q2):
            queryset_list = queryset_list.filter(
            Q(category_iexact=q0)&
            Q(board_iexact=q1)&
            Q(standard_iexact=q2)
            ).values("subject").distinct()
        return queryset_list

class GroupingLessonsAPIView(ListAPIView):
    queryset = Grouping.objects.all()
    serializer_class = GroupingLessonsSerializer
    def get_queryset(self,*args,**kwargs):
        queryset_list = Grouping.objects.all()
        q0 = self.request.GET.get("category")
        q1 = self.request.GET.get("board")
        q2 = self.request.GET.get("std")
        q3 = self.request.GET.get("sub")
        if (q1 and q2 and q3):
            queryset_list = queryset_list.filter(
            Q(category_iexact=q0)&
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
