import datetime

from django.db import models
from django.utils import timezone


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
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        """Return choice text."""
        return self.choice_text
    