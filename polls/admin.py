from polls.models import Poll
from django.contrib import admin
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('questions', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['questions']
    date_hierarchy = 'pub_date'

    inlines = [ChoiceInline]

admin.site.register(Poll,PollAdmin)
