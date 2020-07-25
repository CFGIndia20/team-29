from django.contrib import admin
from .models import test_questions, test_results
# Register your models here.

class test_questionsAdmin(admin.ModelAdmin):
    list_display = ('question_Id', 'question', 'option1', 'option2', 'option3', 'option4', 'ans')
    search_fields = ('question',)
    ordering = ('question_Id',)
    list_filter = ()

admin.site.register(test_questions, test_questionsAdmin)

class test_resultsAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'marks', 'is_pass', 'is_aboveAvg',)
    ordering = ('marks',)
    list_filter = ('is_pass', 'is_aboveAvg',)

admin.site.register(test_results, test_resultsAdmin)
