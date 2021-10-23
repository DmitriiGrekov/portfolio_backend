from django.db.models import fields
from rest_framework import serializers
from .models import SiteModel


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteModel
        fields = ('id',
                  'name',
                  'desc',
                  'link_to_site',
                  'link_to_rep',
                  'image')