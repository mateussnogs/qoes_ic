from django.contrib import admin
from .models import Feedback, StressFeedback, Categories
# Register your models here.



class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['num_sessao', 'num_video_preferido', 'incomodo', 'interesse1', 'interesse2', 'created_date', 'justificativa', 'email', 'session_id', 'comment', 'english']
    search_fields = ['justificativa', 'num_sessao']
    list_filter = ['created_date']

class StressFeedbackAdmin(admin.ModelAdmin):
    list_display = ['num_sessao', 'estresse', 'justificativa', 'created_date', 'email', 'session_id', 'english']
    search_fields = ['justificativa', 'estresse']
    list_filter = ['created_date']

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['comedia', 'esporte', 'documentario', 'musica', 'email', 'english', 'session_id', 'created_date']

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(StressFeedback, StressFeedbackAdmin)
admin.site.register(Categories, CategoriesAdmin)
