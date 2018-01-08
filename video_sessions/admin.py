from django.contrib import admin
from .models import Feedback
# Register your models here.



class FeedbackAdmin(admin.ModelAdmin):

    list_display = ['author', 'num_sessao', 'num_video_preferido', 'created_date', 'text']
    search_fields = ['text', 'author', 'num_sessao']
    list_filter = ['created_date']


admin.site.register(Feedback, FeedbackAdmin)
