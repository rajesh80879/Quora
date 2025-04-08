from django.urls import path
from .views import (
    home_view,
    register_view,
    login_view,
    logout_view,
    add_question,
    question_detail,
    like_answer,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("add-question/", add_question, name="add_question"),
    path("question/<uuid:question_id>/", question_detail, name="question_detail"),
    path("like-answer/<uuid:answer_id>/", like_answer, name="like_answer"),
]
