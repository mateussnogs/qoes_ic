from django.contrib import admin
from .models import Feedback, StressFeedback
# Register your models here.



class FeedbackAdmin(admin.ModelAdmin):

    list_display = ['num_sessao', 'num_video_preferido', 'incomodo', 'interesse1', 'interesse2', 'created_date', 'justificativa', 'email']
    search_fields = ['justificativa', 'num_sessao']
    list_filter = ['created_date']

class StressFeedbackAdmin(admin.ModelAdmin):

    list_display = ['num_sessao', 'estresse', 'justificativa', 'created_date', 'email']
    search_fields = ['justificativa', 'estresse']
    list_filter = ['created_date']

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(StressFeedback, StressFeedbackAdmin)
