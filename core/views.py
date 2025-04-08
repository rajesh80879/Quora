import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Question, Answer
from .forms import RegisterForm, QuestionForm, AnswerForm

logger = logging.getLogger(__name__)


def register_view(request):
    try:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Account created successfully!")
                logger.info(f"User registered successfully: {user.name}")
                return redirect("home")
            else:
                logger.error(f"Registration form invalid: {form.errors}")
                messages.error(
                    request, "Registration failed. Please correct the errors."
                )
        else:
            form = RegisterForm()
    except Exception as e:
        logger.error(f"Error in register_view: {e}")
        messages.error(request, "Something went wrong during registration.")
    return render(request, "register.html", {"form": form})


def login_view(request):
    try:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Welcome {user.name}!")
                logger.info(f"User logged in: {user.name}")
                return redirect("home")
            else:
                logger.error(f"Failed login attempt for email: {email}")
                messages.error(request, "Invalid email or password.")
    except Exception as e:
        logger.error(f"Error in login_view: {e}")
        messages.error(request, "Something went wrong during login.")
    return render(request, "login.html")


def logout_view(request):
    try:
        logout(request)
        messages.success(request, "Logged out successfully!")
        logger.info("User logged out successfully.")
    except Exception as e:
        logger.error(f"Error in logout_view: {e}")
        messages.error(request, "Something went wrong during logout.")
    return redirect("login")


@login_required
def home_view(request):
    try:
        questions = Question.objects.all().order_by("-created_at")
    except Exception as e:
        logger.error(f"Error fetching questions: {e}")
        questions = []
        messages.error(request, "Failed to load questions.")
    return render(request, "home.html", {"questions": questions})


@login_required
def add_question(request):
    try:
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            messages.success(request, "Question posted successfully!")
            logger.info(f"Question posted by: {request.user.name}")
            return redirect("home")
        elif request.method == "POST":
            messages.error(request, "Failed to post the question.")
            logger.error("Invalid question form submitted.")
    except Exception as e:
        logger.error(f"Error in add_question: {e}")
        messages.error(request, "Something went wrong while posting the question.")
    return render(request, "add_question.html", {"form": form})


@login_required
def question_detail(request, question_id):
    try:
        question = get_object_or_404(Question, id=question_id)
        answers = Answer.objects.filter(question=question)
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            messages.success(request, "Answer posted successfully!")
            logger.info(f"Answer posted by: {request.user.name}")
            return redirect("question_detail", question_id=question.id)
    except Exception as e:
        logger.error(f"Error in question_detail: {e}")
        messages.error(request, "Something went wrong while posting the answer.")
    return render(
        request,
        "question_detail.html",
        {"question": question, "answers": answers, "form": form},
    )


@login_required
def like_answer(request, answer_id):
    try:
        answer = get_object_or_404(Answer, id=answer_id)
        answer.likes.add(request.user)
        messages.success(request, "You liked an answer!")
        logger.info(f"Answer liked by: {request.user.name}")
    except Exception as e:
        logger.error(f"Error in like_answer: {e}")
        messages.error(request, "Something went wrong while liking the answer.")
    return redirect("question_detail", question_id=answer.question.id)
