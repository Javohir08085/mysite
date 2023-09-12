from django.urls import path
from .views import ListQuestionsView


urlpatterns = [
    
    path('all_question/',ListQuestionsView.as_view)
    
    # path('all_question/',get_all_question),
    # path('detail_question/<int:question_id>',detail_question)

    # path('all/',all_questions),
    # path('detail/<int:question_id>',detail),
    
]