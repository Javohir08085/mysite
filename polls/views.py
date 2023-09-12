from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Question
from .serializers import Questionserializers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ListQuestionsView(APIView):
    def get(self,request):
        return Response({'data':'APIView is working'})

# def get_all_question(request):
#     all_data = Question.objects.all()
#     serializer = Questionserializers(all_data,many=True)
    # resoult = []
    # for question in all_data:
    #     resoult.append({
    #         'question_text': question.question_text,
    #         'pub_date' : question.pub_date
    #     })

    # return JsonResponse(serializer.data,safe=False)

def detail_question(request,question_id):
    question = get_object_or_404(Question,id=question_id)
    serializer = Questionserializers(question)
    # data = {
    #     'question_text': question.question_text,
    #     'pub_date' : question.pub_date
    # }
    return JsonResponse(serializer)

# def all_questions(request):
#     return HttpResponse("all questions")

# def detail(request,question_id):
#     try:
#         question  = Question.objects.get(id=question_id)

#         return HttpResponse(f"id:{question.id}, question_text:{question.question_text},pub_date:{question.pub_date} ")
#     except Question.DoesNotExist:
#         return  HttpResponse(f"{question_id} not found")