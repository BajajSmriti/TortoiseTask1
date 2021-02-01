from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
from rest_framework import viewsets
import sys
from .serializers import *
from .models import *
import json


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all().order_by('name')
    serializer_class = MerchantSerializer
    # search_fields = ('name', 'id',)

def activePlansMerchant(request, user_id=None, user=None):
    """Method to list active plans at a Merchant"""
    try:
        if(user_id is not None):
            merchant = get_object_or_404(Merchant, pk=user_id)
        else:
            merchant = get_object_or_404(Merchant, name=user)    
    except Exception as e:
            raise e

    try:
        plans=[]
        for i in Plan.objects.filter(user_id= merchant.__str__(), plan_status='active'):
            plans.append(i.uuid)
    except Exception as e:
        raise e
    body = json.dumps({"list_active_plans" : plans})
    
    return HttpResponse(body)

def totalActivePlansMerchant(request, user_id=None, user=None):
    """Method to calculate total amount of active plans at a Merchant"""
    try:
        if(user_id is not None):
            merchant = get_object_or_404(Merchant, pk=user_id)
        else:
            merchant = get_object_or_404(Merchant, name=user)    
    except Exception as e:
            raise e
    try:
        total = 0
        for i in Plan.objects.filter(user_id= merchant.__str__(), plan_status='active'):
            total+=i.total_paid_amount
    except Exception as e:
        raise e
    body = json.dumps({"Total_Value_Active" : total})
    
    return HttpResponse(body)

def totalVoidedPlansMerchant(request, user_id=None, user=None):
    """Method to calculate total amount of voided plans at a Merchant"""
    try:
        if(user_id is not None):
            merchant = get_object_or_404(Merchant, pk=user_id)
        else:
            merchant = get_object_or_404(Merchant, name=user)    
    except Exception as e:
            raise e
    try:
        total = 0
        for i in Plan.objects.filter(user_id= merchant.__str__(), plan_status='voided'):
            total+=i.total_paid_amount
    except Exception as e:
        raise e
    body = json.dumps({"Total_Value_Voided" : total})
    
    return HttpResponse(body)

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TermsInfoViewSet(viewsets.ModelViewSet):
    queryset = TermsInfo.objects.all()
    serializer_class = TermsInfoSerializer

class RedemptionInfoViewSet(viewsets.ModelViewSet):
    queryset = RedemptionInfo.objects.all()
    serializer_class = RedemptionInfoSerializer

class CancellationInfoViewSet(viewsets.ModelViewSet):
    queryset = CancellationInfo.objects.all()
    serializer_class = CancellationInfoSerializer