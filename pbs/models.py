from django.db import models

class Birim(models.Model):
    birim_turuSecenekleri = (
        ('A', 'Akademik'),
        ('I', 'İdari')
    )

    birim_kategoriSecenekleri = (
        ('F', 'Fakülte'),
        ('M', 'MYO'),
        ('Y', 'Yüksekokul'),
        ('E', 'Enstitü'),
        ('K', 'Koordinatörlük'),
        ('R', 'Rektörlüğe Bağlı Birim')
    )

    birim_turu = models.CharField(max_length=1, choices=birim_turuSecenekleri, verbose_name='Birim Türü')
    birim_kategori = models.CharField(max_length=1, choices=birim_kategoriSecenekleri, verbose_name='Birim Kategori')
    adi = models.CharField(max_length=200)
    ing_adi = models.CharField(max_length=200)
    birim_kodu = models.CharField(max_length=2)
    birim_kodu2 = models.CharField(max_length=10)
    genel_bilgi = models.TextField()

    def __str__(self):
        return self.adi
    class Meta:
        verbose_name = 'Birim'
        verbose_name_plural = 'Birimler'

class Bolum(models.Model):
    birim = models.ForeignKey(Birim, on_delete=models.PROTECT, default=1, verbose_name='Fakülte/MYO')
    adi = models.CharField(max_length=200)
    ing_adi = models.CharField(max_length=200)
    alt_birim_kodu = models.CharField(max_length=2)
    alt_birim_kodu2 = models.CharField(max_length=10)
    genel_bilgi = models.TextField()


    def __str__(self):
        return self.adi
    class Meta:
        verbose_name = 'Bölüm'
        verbose_name_plural = 'Bölümler'

class Ana_Bilim_Dali(models.Model):

    fakulte=models.ForeignKey(Birim, on_delete=models.PROTECT)
    bolum=models.ForeignKey(Bolum, on_delete=models.PROTECT)
    adi=models.CharField(max_length=100)
    ing_adi=models.CharField(max_length=100)

    def __str__(self):
        return self.adi
    class Meta:
        verbose_name = 'Anabilim Dalı'
        verbose_name_plural = 'Anabilim Dalları'

class Personel(models.Model):

    birim = models.ForeignKey(Birim, on_delete=models.PROTECT, default=1, verbose_name='Birimi')
    bolum = models.ForeignKey(Bolum, on_delete=models.PROTECT, default=1, verbose_name='Bölümü')
    ana_bilim_dali = models.ForeignKey(Ana_Bilim_Dali, on_delete=models.PROTECT, default=1, verbose_name="Ana Bilim Dalı")
    adi_soyadi = models.CharField(max_length=50)
    sicil = models.CharField(max_length=5)
    telefon = models.CharField(max_length=7)
    e_posta = models.CharField(max_length=30)
    genel_bilgi = models.TextField()


    def __str__(self):
        return self.adi_soyadi

# Create your models here.
class Transaksi(models.Model):
    deskripsi = models.TextField()
    jumlah = models.DecimalField(max_digits=20, decimal_places=2)
    dibuat = models.DateField(auto_now_add=True)
    diubah = models.DateField(auto_now=True)
    pemilik = models.ForeignKey('auth.User', null=False, on_delete=models.PROTECT)

