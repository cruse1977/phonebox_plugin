from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from ..models import Number
from tenancy.api.nested_serializers import NestedTenantSerializer
from dcim.api.nested_serializers import NestedRegionSerializer
from circuits.api.nested_serializers import NestedProviderSerializer
from extras.api.serializers import TaggedObjectSerializer
from .nested_serializers import NestedNumberSerializer


class NumberSerializer(TaggedObjectSerializer, serializers.ModelSerializer):

    tenant = NestedTenantSerializer(required=True, allow_null=False)
    region = NestedRegionSerializer(required=False, allow_null=True)
    provider = NestedProviderSerializer(required=False, allow_null=True)
    forward_to = NestedNumberSerializer(required=False, allow_null=True)

    class Meta:
        model = Number
        fields = [
            "id", "number", "tenant", "region", "forward_to", "description", "provider", "tags",
        ]
