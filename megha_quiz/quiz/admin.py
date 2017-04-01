from django.contrib.admin import ModelAdmin
from django.contrib import admin
from quiz.models import Question

class QuestionAdmin(ModelAdmin):
    search_fields = ['question', 'option_1', 'option_2', 'option_3']
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Question, QuestionAdmin)