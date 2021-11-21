# Serializers are used to 
# validate incoming input from the user and
# specify output from the different responses for the user

from rest_framework import serializers
from .models import Campaign, Subscriber


class CampaignSerializer(serializers.ModelSerializer):
    
    #specify fields to include in serializer class
    class Meta:
        model=Campaign
        fields="__all__"

class SubscriberSerializer(serializers.ModelSerializer): #??
    
    class Meta:
        model=Subscriber
        fields="__all__"