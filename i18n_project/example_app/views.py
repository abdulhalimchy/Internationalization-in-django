from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Question
from .serializers import QuestionSerializer

class WelcomeMessageView(APIView):
    
    def get(self, request):
        sentence = "You are welcome"

        data = {
            #In this case language will be dectected from 'Accepted-Language' of  request.headers with the help of 'django.middleware.locale.LocaleMiddleware'
            "message": _(sentence)
        }

        return Response(data=data, status=status.HTTP_200_OK)


class QuestionListView(generics.ListAPIView):
    #In this case language will be dectected from 'Accepted-Language' of  request.headers with the help of 'django.middleware.locale.LocaleMiddleware'
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer