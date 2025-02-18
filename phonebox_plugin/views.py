#!./venv/bin/python

from netbox.views import generic
from .models import Number, VoiceCircuit
from . import filters
from . import forms
from . import tables

from django.conf import settings
from packaging import version


class NumberListView(generic.ObjectListView):
    queryset = Number.objects.all()
    filterset = filters.NumberFilterSet
    filterset_form = forms.NumberFilterForm
    table = tables.NumberTable
    #template_name = "phonebox_plugin/number_list_view.html"
    

class NumberView(generic.ObjectView):
    queryset = Number.objects.prefetch_related('tenant')
    template_name = "phonebox_plugin/number.html"
    
class NumberEditView(generic.ObjectEditView):
    queryset = Number.objects.all()
    form = forms.NumberEditForm
    template_name = "phonebox_plugin/add_number_3.x.html"
    
class NumberBulkEditView(generic.BulkEditView):
    queryset = Number.objects.prefetch_related('tenant')
    filterset = filters.NumberFilterSet
    table = tables.NumberTable
    form = forms.NumberBulkEditForm


class NumberDeleteView(generic.ObjectDeleteView):
    queryset = Number.objects.all()
    default_return_url = "plugins:phonebox_plugin:list_view"


class NumberBulkDeleteView(generic.BulkDeleteView):
    queryset = Number.objects.filter()
    filterset = filters.NumberFilterSet
    table = tables.NumberTable
    default_return_url = "plugins:phonebox_plugin:list_view"


class NumberBulkImportView(generic.BulkImportView):
    queryset = Number.objects.all()
    model_form = forms.NumberCSVForm
    table = tables.NumberTable


class VoiceCircuitListView(generic.ObjectListView):
    queryset = VoiceCircuit.objects.all()
    filterset = filters.VoiceCircuitFilterSet
    filterset_form = forms.VoiceCircuitFilterForm
    table = tables.VoiceCircuitTable
    template_name = "phonebox_plugin/voice_circuit_list_view_4.x.html"
    

class VoiceCircuitView(generic.ObjectView):
    queryset = VoiceCircuit.objects.prefetch_related('tenant')
    template_name = "phonebox_plugin/voice_circuit_3.x.html"
    

class VoiceCircuitEditView(generic.ObjectEditView):
    queryset = VoiceCircuit.objects.all()
    form = forms.VoiceCircuitEditForm
    template_name = "phonebox_plugin/add_voice_circuit_3.x.html"
    
class VoiceCircuitBulkEditView(generic.BulkEditView):
    queryset = VoiceCircuit.objects.prefetch_related('tenant')
    filterset = filters.VoiceCircuitFilterSet
    table = tables.VoiceCircuitTable
    form = forms.VoiceCircuitBulkEditForm


class VoiceCircuitDeleteView(generic.ObjectDeleteView):
    queryset = VoiceCircuit.objects.all()
    default_return_url = "plugins:phonebox_plugin:voice_circuit_list_view"


class VoiceCircuitBulkDeleteView(generic.BulkDeleteView):
    queryset = VoiceCircuit.objects.filter()
    filterset = filters.VoiceCircuitFilterSet
    table = tables.VoiceCircuitTable
    default_return_url = "plugins:phonebox_plugin:voice_circuit_list_view"


class VoiceCircuitBulkImportView(generic.BulkImportView):
    queryset = VoiceCircuit.objects.all()
    model_form = forms.VoiceCircuitCSVForm
    table = tables.VoiceCircuitTable
