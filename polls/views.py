from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Choice, Question, Vote


def showtime(request) -> HttpResponse:
    thai_time = timezone.localtime()
    message = f"<p>Thai Time: {thai_time}</p>"
    return HttpResponse(message)


class IndexView(generic.ListView, LoginRequiredMixin):
    login_url = '/accounts/login/'
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def dispatch(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        if not question.can_vote():
            messages.error(request, "Voting is not ready for this poll")
            return redirect(reverse('polls:index'))
        else:
            user = request.user
            other_vote = list(Vote.objects.filter(user=user).filter(choice__question=question))
            if len(other_vote)>0:
                latest_vote_choice = other_vote[-1].choice
            else:
                latest_vote_choice = None
            
            return render(request, self.template_name, {'question': question, 'latest_vote_choice': latest_vote_choice})
            # return super().get(request, *args, **kwargs)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


@login_required
def vote(request, question_id):
    """Submit button, process the poll when vote button is clicked."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        user = request.user
        total_vote = []
        for choice in question.choice_set.all():
            for vote in choice.vote_set.all():
                total_vote.append(vote)
        other_vote = list(Vote.objects.filter(
            user=user).filter(choice__question=question))
        if len(other_vote) > 0:
            if other_vote[-1] in total_vote:
                other_vote[-1].delete()
        vote = Vote(user=user, choice=selected_choice)
        vote.save()

        # selected_choice.votes += 1
        # selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
