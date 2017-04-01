from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    corrent_answer_choices = [
        (1, '1'),
        (2, '2'),
        (3, '3')
    ]
    question = models.TextField(max_length=1000, verbose_name='Question',)
    option_1 = models.CharField(max_length=100, verbose_name='Choice 1',)
    option_2 = models.CharField(max_length=100, verbose_name='Choice 2',)
    option_3 = models.CharField(max_length=100, verbose_name='Choice 3',)
    correct_answer = models.IntegerField(choices=corrent_answer_choices, verbose_name='Correct answer',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = ('questions')
