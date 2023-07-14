from django.contrib import admin


from .models import Choice, Question

# Tried to use list_display on Choice page but didnt work:

# class ChoiceAdmin(admin.ModelAdmin):
    # fields = ["choice_text", "votes"]
    # list_display = ["choice_text", "votes"]


## Add inlines when you need an admin component to sit inside another:

## Stacked Inline:  (to much whitespace for this purpose)

# class ChoiceInLine(admin.StackedInline):
#     model = Choice
#     extra = 3

## Tabular Inline:

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["question_text","pub_date"]
    fieldsets = [
        (None, {"fields": ["question_text"]}), ##first argument is name of field - None in this case
        ("Date Information", {"fields": ["pub_date"]}),

    ]

    inlines = [ChoiceInLine]

    list_display = ["question_text", "pub_date", "was_published_recently"]

    list_filter = ["pub_date"]

    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

