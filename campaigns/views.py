from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Campaign, Subscriber
from .serializers import SubscriberSerializer, CampaignSerializer



# Create your views here.
# We will use generic views to implement a thinner API(elegant less code)

# Retrieving all our campaigns
class CampaignListAPIView(generics.ListAPIView):
    serializer_class = CampaignSerializer
    
    # function to query the records returned in this list
    def get_queryset(self):
        return  Campaign.objects.all()


class CampaignDetailAPIView(generics.GenericAPIView):
    serializer_class=CampaignSerializer

    def get(self, request, slug):

        query_set = Campaign.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)
        
        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)

class SubscribeToCampaignAPIView(generics.CreateAPIView):
    
    serializer_class = SubscriberSerializer
    
    def get_queryset(self):
        
        return Subscriber.object.all()