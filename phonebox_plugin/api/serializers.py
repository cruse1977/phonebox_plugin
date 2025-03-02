from django.contrib.contenttypes.models import ContentType
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from ..models import Number, VoiceCircuit
from tenancy.api.serializers import TenantSerializer
from dcim.api.serializers import SiteSerializer, RegionSerializer, SiteSerializer
from circuits.api.serializers import ProviderSerializer
from netbox.api.fields import ContentTypeField
from utilities.api import get_serializer_for_model
from ..choices import VOICE_CIRCUIT_ASSIGNMENT_MODELS
from netbox.api.serializers import NetBoxModelSerializer


class NumberSerializer(NetBoxModelSerializer):

    label = serializers.CharField(source='number', read_only=True)
    tenant = TenantSerializer(required=True, allow_null=False, nested=True)
    region = RegionSerializer(required=False, allow_null=True, nested=True)
    site = SiteSerializer(required=False, allow_null=True, nested=True)
    provider = ProviderSerializer(required=False, allow_null=True, nested=True)
    forward_to = serializers.PrimaryKeyRelatedField(queryset=Number.objects.all(), required=False, allow_null=True)


    class Meta:
        model = Number
        fields = (
            "id", "url", "display", "label", "number", "tenant", "site", "region", "forward_to", "description", "provider", "tags",
        )
        brief_fields = ("id", "url", "number", "display")


class VoiceCircuitSerializer(NetBoxModelSerializer):

    label = serializers.CharField(source='voice_circuit', read_only=True)
    tenant = TenantSerializer(required=True, allow_null=False, nested=True)
    region = RegionSerializer(required=False, allow_null=True, nested=True)
    site = SiteSerializer(required=False, allow_null=True, nested=True)
    provider = ProviderSerializer(required=False, allow_null=True, nested=True)
    assigned_object_type = ContentTypeField(
        queryset=ContentType.objects.filter(VOICE_CIRCUIT_ASSIGNMENT_MODELS),
        required=True,
        allow_null=False
    )
    assigned_object = serializers.SerializerMethodField(read_only=True)

    @extend_schema_field(serializers.JSONField(allow_null=True))
    def get_assigned_object(self, obj):
        if obj.assigned_object is None:
            return None
        serializer = get_serializer_for_model(obj.assigned_object)
        context = {'request': self.context['request']}
        return serializer(obj.assigned_object, context=context).data

    class Meta:
        model = VoiceCircuit
        fields = (
            "id", "url", "label", "display", "name", "voice_circuit_type", "tenant", "region", "site", "description",
            'assigned_object_type','assigned_object_id', 'assigned_object',
            "sip_source", "sip_target", "provider", "tags",
        )
        brief_fields = ("id", "url", "name", "display")
