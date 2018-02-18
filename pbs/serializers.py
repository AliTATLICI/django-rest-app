from pbs.models import Birim

from rest_framework import serializers

class BirimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Birim
        fields=('birim_turu','birim_kategori','adi', 'birim_kodu')
