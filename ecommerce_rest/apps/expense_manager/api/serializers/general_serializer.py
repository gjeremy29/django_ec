from rest_framework import serializers

from apps.products.models import Product
from apps.expense_manager.models import *

class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        exclude = ('id', 'ruc', 'business_name', 'address')
          
class VoucherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voucher
        exclude = ('id', 'name')

class PaymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentType
        exclude = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('id', 'name')