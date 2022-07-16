from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from main.models import Survey
from main.forms import SurveyForm


def index(request):
    return render(request, "lewagon/index.html")


def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    post_data = request.POST if request.method == "POST" else None
    form = SurveyForm(survey, post_data)

    url = reverse("show-survey", args=(id,))
    if form.is_bound and form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Submissions saved.')
        return redirect(url)

    context = {
        "survey": survey,
        "form": form,
    }
    return render(request, "lewagon/survey.html", context)
