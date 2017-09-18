from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from rest_framework import viewsets
from .Serializers import *

from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import *
from .forms import *

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = CustomerAddressSerializer
class AgentAddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AgentAddressSerializer
class AgentReferalViewSet(viewsets.ModelViewSet):
    queryset = AgentReferal.objects.all()
    serializer_class = AgentReferalSerializer
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
class AgentList(ListView):
    model = Agent

class CustomerList(ListView):
    model = Customer


class CustomerCreate(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'mobile_number', 'phone_number', 'email_id']


class CustomerAddressCreate(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'mobile_number', 'phone_number', 'email_id']
    success_url = reverse_lazy('customer-list')

    def get_context_data(self, **kwargs):
        data = super(CustomerAddressCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address'] = CustomerAddressFormSet(self.request.POST)
        else:
            data['address'] = CustomerAddressFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if address.is_valid():
                address.instance = self.object
                address.save()
        return super(CustomerAddressCreate, self).form_valid(form)


class CustomerUpdate(UpdateView):
    model = Customer
    success_url = '/'
    fields = ['first_name', 'last_name',  'mobile_number', 'phone_number', 'email_id']


class CustomerAddressUpdate(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name',  'mobile_number', 'phone_number', 'email_id']
    success_url = reverse_lazy('customer-list')

    def get_context_data(self, **kwargs):
        data = super(CustomerAddressUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address'] = CustomerAddressFormSet(self.request.POST, instance=self.object)
        else:
            data['address'] = CustomerAddressFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if address.is_valid():
                address.instance = self.object
                address.save()
        return super(CustomerAddressUpdate, self).form_valid(form)


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')

def agentproperty(request):
    form = PropertyTypeForm()

    if request.method == "POST":
        form = PropertyTypeForm(request.POST)
        if form.is_valid():
            p = PropertyType ()
            p.description = form.cleaned_data["description"]
            p.save()

        else:
            form = PropertyTypeForm()

    ag = PropertyType.objects.all()
    return render(request, "agentproperty.html", {"agentproperty": ag, "form": form})
class AgentCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', ' experience', 'agent_notes',
              'mobile_number','phone_number','email_id', 'property_type']

class AgentAddrLocArefCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', ' experience', 'agent_notes',
              'mobile_number','phone_number','email_id', 'property_type']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddrLocArefCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['location'] = LocationFormSet(self.request.POST)
            data['address'] = AgentAddressFormSet(self.request.POST)
            data['agentreferal'] = AgentReferalFormSet(self.request.POST)
        else:
            data['location'] = LocationFormSet()
            data['address'] = AgentAddressFormSet()
            data['agentreferal'] = AgentReferalFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        location = context['location']
        address = context['address']
        agentreferal = context['agentreferal']
        with transaction.atomic():
            self.object = form.save()

            if location.is_valid() and address.is_valid() and agentreferal.is_valid():
                location.instance = self.object
                address.instance = self.object
                agentreferal.instance = self.object
                location.save()
                address.save()
                agentreferal.save()
        return super(AgentAddrLocArefCreate, self).form_valid(form)

class AgentUpdate(UpdateView):
    model = Agent
    success_url = '/'
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', ' experience',
              'agent_notes', 'mobile_number','phone_number','email_id', 'property_type']


class AgentAddrLocArefUpdate(UpdateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', ' experience',
              'agent_notes', 'mobile_number','phone_number','email_id', 'property_type']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddrLocArefUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['location'] = LocationFormSet(self.request.POST, instance=self.object)
            data['address'] = AgentAddressFormSet(self.request.POST, instance=self.object)
            data['agentreferal'] = AgentReferalFormSet(self.request.POST, instance=self.object)
        else:
            data['location'] = LocationFormSet(instance=self.object)
            data['address'] = AgentAddressFormSet(instance=self.object)
            data['agentreferal'] = AgentReferalFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        location = context['location']
        address = context['address']
        agentreferal = context['agentreferal']
        with transaction.atomic():
            self.object = form.save()

            if location.is_valid() and address.is_valid() and agentreferal.is_valid():
                location.instance = self.object
                address.instance = self.object
                agentreferal.instance = self.object
                location.save()
                address.save()
                agentreferal.save()

        return super(AgentAddrLocArefUpdate, self).form_valid(form)


class AgentDelete(DeleteView):
    model = Agent
    success_url = reverse_lazy('agent-list')
