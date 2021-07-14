from django.contrib import admin

from .models import Sentiment

# Register your models here.

# admin.site.register(Sentiment)

# Define the admin class
@admin.register(Sentiment)
class SentimentAdmin(admin.ModelAdmin):
    list_filter = ['emotion']

    fieldsets = (
        ('Oración', {
            'fields': ['sentence']
        }),
        ('Emoción', {
            'fields': ['emotion']
        }),        
    )

