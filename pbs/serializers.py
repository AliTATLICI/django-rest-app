from . import models

from rest_framework import serializers

class BirimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.Birim
        fields=('birim_turu','birim_kategori','adi', 'birim_kodu')

class TransaksiSeraializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaksi
        fields = '__all__'
        read_only_fields = ('dibuat', 'diubah', 'pemilik')
