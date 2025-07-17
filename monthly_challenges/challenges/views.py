from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "feburary": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day",
    "december": "Learn Django for at least 20 minutes every day!"
}
# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())  # key를 사용해서 숫자를 받으면 월로 바꾸기

    if month > len(months):
        # 입력받은 숫자가 12보다 크면 에러 메세지 출력
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]  # index 0
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)  # redirect


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
