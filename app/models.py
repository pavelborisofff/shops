from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
        db_table = 'cities'
        ordering = ('name',)


class Street(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE,related_name='city_street')

    def __str__(self):
        return f'{self.name} ({self.city})'

    class Meta:
        verbose_name_plural = 'Streets'
        db_table = 'streets'
        ordering = ('name',)


class Shop(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Shop ID')
    name = models.CharField(max_length=100, null=False, blank=False)
    city = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='city_shop')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='street_shop')

    class Meta:
        verbose_name_plural = 'Shops'
        db_table = 'shops'
        ordering = ('name',)

    @property
    def address(self):
        return f'{self.street}, {self.city}'

    def __str__(self):
        return f'{self.name} ({self.address})'


# class House(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name='House ID')
#     number = models.CharField(max_length=10, null=False, blank=False, verbose_name='House number')
#     street = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name='Street name', related_name='street_house')
#
#     def __str__(self):
#         return f'{self.number} ({self.street})'
#
#     class Meta:
#         verbose_name_plural = 'Houses'
#         db_table = 'houses'