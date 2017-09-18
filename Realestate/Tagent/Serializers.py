from rest_framework import serializers
from . models import *
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =['customer_id','first_name','last_name','mobile_number','phone_number','email_id']
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields =['agent_id','first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence', 'agent_notes',
              'mobile_number','phone_number','email_id','media_name','media_path','property_type']
class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields =['customer_id','address1','address2','city','state','landmark','pincode']

class AgentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields =['agent_id','address1','address2','city','state','landmark','pincode']
class AgentReferalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentReferal
        fields ="__all__"
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields ="__all__"
class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields ="__all__"