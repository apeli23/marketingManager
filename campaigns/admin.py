from django.contrib import admin
from .models import Campaign, Subscriber


# Create modal admin class
class CampaignModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_per_page = 10;


class SubscriberModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'campaign', 'created_at')
    search_fields = ('email', 'campaign__title', 'created_at')
    list_per_page = 10

# Register your models here.
admin.site.register(Campaign, CampaignModelAdmin)
admin.site.register(Subscriber)
