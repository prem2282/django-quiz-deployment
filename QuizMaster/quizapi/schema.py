import graphene

from graphene_django.types import DjangoObjectType

from quizapi.models import QuestionBank, Grouping, PMPQuestionBank, CodeBank, UserQuiz, UserDetails, UserPackage, Constants


class QuestionBankType(DjangoObjectType):
    class Meta:
        model = QuestionBank

class GroupingType(DjangoObjectType):
    class Meta:
        model = Grouping

class PMPQuestionBankType(DjangoObjectType):
    class Meta:
        model = PMPQuestionBank

class CodeBankType(DjangoObjectType):
    class Meta:
        model = CodeBank

class UserQuizType(DjangoObjectType):
    class Meta:
        model = UserQuiz

class UserDetailsType(DjangoObjectType):
    class Meta:
        model = UserDetails

class UserPackageType(DjangoObjectType):
    class Meta:
        model = UserPackage

class Query(object):
    all_questionBank = graphene.List(QuestionBankType)
    all_grouping = graphene.List(GroupingType)
    all_PMPQuestionBank = graphene.List(PMPQuestionBankType)
    all_userQuiz = graphene.List(UserQuizType)
    all_codeBank = graphene.List(CodeBankType)
    all_userDetails = graphene.List(UserDetailsType)
    all_userPackage = graphene.List(UserPackageType)
    userDetails = graphene.Field(UserDetailsType,userId=graphene.String())
    questionBank = graphene.List(QuestionBankType,
                                  category=graphene.String(),
                                  board=graphene.String(),
                                  standard=graphene.String(),
                                  subject=graphene.String(),
                                  lessonNum=graphene.String()
                                  )

    def resolve_userDetails(self, info, **args):
        userId = args.get('userId')
        if userId is not None:
            print(userId)
            return UserDetails.objects.get(userId=userId)

        return None

    def resolve_questionBank(self,info, **args):
        category = args.get('category')
        board = args.get('board')
        standard= args.get('standard')
        subject=args.get('subject')
        lessonNum=args.get('lessonNum')

        if category is not None:
            if board is not None:
                if standard is not None:
                    if subject is not None:
                        if lessonNum is not None:
                            return QuestionBank.objects.filter(category=category,
                                                            board=board,
                                                            standard=standard,
                                                            subject=subject,
                                                            lessonNum=lessonNum
                                                            )

                        return QuestionBank.objects.filter(category=category,
                                                        board=board,
                                                        standard=standard,
                                                        subject=subject
                                                        )
                    return QuestionBank.objects.filter(category=category,
                                                    board=board,
                                                    standard=standard
                                                    )
                return QuestionBank.objects.filter(category=category,
                                                board=board)
            return QuestionBank.objects.filter(category=category)

        return QuestionBank.objects.all()



    def resolve_all_questionBank(self, info, **kwargs):
        return QuestionBank.objects.all()

    def resolve_all_grouping(self, info, **kwargs):
        return Grouping.objects.all()

    def resolve_all_PMPQuestionBank(self, info, **kwargs):
        return PMPQuestionBank.objects.all()

    def resolve_all_userQuiz(self, info, **kwargs):
        return UserQuiz.objects.all()

    def resolve_all_userDetails(self, info, **kwargs):
        return UserDetails.objects.all()

    def resolve_all_userPackage(self, info, **kwargs):
        return UserPackage.objects.all()
