from django.contrib import admin

from polls.models import Question, Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question_text', 'get_choices', 'was_published_recently', 'pub_date')
    list_display_links = ('pk', )
    list_editable = ('question_text', )
    list_filter = ('pub_date', )
    search_fields = ('question_text', 'pub_date')

    fieldsets = (
        (
            'Question', {
                'fields': ('question_text', )
            }
        ),
        (
            'When', {
                'fields': ('pub_date', )
            }
        )
    )


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'choice_text', 'votes')
    list_display_links = ('pk', 'choice_text')
    list_filter = ('question__question_text', )
    search_fields = ('choice_text', )

    fieldsets = (
        (
            'Question', {
                'fields': ('question', )
            }
        ),
        (
            'Choice', {
                'fields': ('choice_text', 'votes')
            }
        )
    )
