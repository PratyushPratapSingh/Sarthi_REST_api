from rest_framework import serializers
from sarthi.models import book


class BookSerializer(serializers.ModelSerializer):

    # In this api if you want to update anything and don't want the other field to write it again then use required=False
    # either in model level and migrate or do it in serializer level
    name = serializers.CharField(required=False)
    class Meta:
        model = book
        fields = '__all__'
