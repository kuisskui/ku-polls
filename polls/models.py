import datetime
from secrets import choice

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    """Question Model."""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date expired', null=True, blank=True)

    def __str__(self):
        """Return question text."""
        return self.question_text

    def was_published_recently(self):
        """Return whether is it published within one day."""
        now = timezone.localtime()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """Return whether is it published."""
        now = timezone.localtime()
        return self.pub_date <= now

    def can_vote(self) -> bool:
        """Current date is ready for voting."""
        now = timezone.localtime()
        if not self.end_date:
            return self.is_published()
        return self.is_published and now <= self.end_date


class Choice(models.Model):
    """Choice Model."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    @property
    def vote(self):
        """Count the number of votes for this choice."""
        return Vote.objects.filter(choice=self).count()

    def __str__(self):
        """Return choice text."""
        return self.choice_text


class Vote(models.Model):
    """A vote by a user for a question."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vote by {self.user.username}, choice : {self.choice.choice_text}"
    
def get_client_ip(request):
    """Get the visitor's IP address using request headers."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip