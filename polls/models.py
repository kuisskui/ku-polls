import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date expired', null=True, blank=True)

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
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
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    