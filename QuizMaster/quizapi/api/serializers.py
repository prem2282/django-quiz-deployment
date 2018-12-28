from rest_framework.serializers import ModelSerializer

from quizapi.models import QuestionBank, Grouping, UserDetails, UserQuiz, PMPQuestionBank, UserPackage, Constants
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','frist_name','last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id','is_staff','is_superuser','is_active','date_joined',)

        def create(self, validated_data):
            user = User.objects.create(
                username = validated_data['username'],
                email = validated_data['email'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name']
            )

            user.set_password(validated_data['password'])
            user.save()

            return user

class UserPackageSerializer(ModelSerializer):
    class Meta:
        model = UserPackage
        fields = '__all__'

class ConstantsSerializer(ModelSerializer):
    class Meta:
        model = Constants
        fields = '__all__'

class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'

class UserQuizSerializer(ModelSerializer):
    class Meta:
        model = UserQuiz
        fields = '__all__'

class PMPQuestionBankSerializer(ModelSerializer):
    class Meta:
        model = PMPQuestionBank
        fields = '__all__'

class PMPQuestionBankIdSerializer(ModelSerializer):
    class Meta:
        model = PMPQuestionBank
        fields = '__all__'

class PMPQuestionBankCreateSerializer(ModelSerializer):
    class Meta:
        model = PMPQuestionBank
        fields = '__all__'

class QuestionBankSerializer(ModelSerializer):
    class Meta:
        model = QuestionBank
        fields = '__all__'

class QuestionBankIdSerializer(ModelSerializer):
    class Meta:
        model = QuestionBank
        fields = '__all__'

class QuestionBankCreateSerializer(ModelSerializer):
    class Meta:
        model = QuestionBank
        fields = '__all__'

class GroupingSerializer(ModelSerializer):
    class Meta:
        model = Grouping
        fields = '__all__'

class GroupingCreateSerializer(ModelSerializer):
    class Meta:
        model = Grouping
        fields = '__all__'

class GroupingBoardSerializer(ModelSerializer):
    class Meta:
        model = Grouping
        fields = ['board']

class GroupingStdSerializer(ModelSerializer):
    class Meta:
        model = Grouping
        fields = ['standard']

class GroupingSubSerializer(ModelSerializer):
    class Meta:
        model = Grouping
        fields = ['subject']

class GroupingLessonsSerializer(ModelSerializer):
    class Meta:
        model = Grouping
        fields = ['lessonNum','lessonName']
