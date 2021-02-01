from rest_framework import serializers

from .models import *

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheme
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TermsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsInfo
        fields = '__all__'

class RedemptionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedemptionInfo
        fields = '__all__'

class CancellationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancellationInfo
        fields = '__all__'