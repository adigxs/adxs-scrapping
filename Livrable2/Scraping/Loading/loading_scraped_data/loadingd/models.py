from django.db import models


# 
# 
# Commande :  python3 manage.py inspectdb

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Address(models.Model):
    idaddress = models.AutoField(db_column='idAddress', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    street = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Address'


class Contain(models.Model):
    idcontain = models.IntegerField(db_column='idContain', primary_key=True)  # Field name made lowercase.
    idshop = models.ForeignKey('Shop', models.DO_NOTHING, db_column='idShop', blank=True, null=True)  # Field name made lowercase.
    idwebsite = models.ForeignKey('Website', models.DO_NOTHING, db_column='idWebsite', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contain'


class Product(models.Model):
    idproduct = models.AutoField(db_column='idProduct', primary_key=True)  # Field name made lowercase.
    idshop = models.ForeignKey('Shop', models.DO_NOTHING, db_column='idShop', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    priceinit = models.FloatField(db_column='priceInit', blank=True, null=True)  # Field name made lowercase.
    pricered = models.FloatField(db_column='priceRed', blank=True, null=True)  # Field name made lowercase.
    stock = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Product'


class Shop(models.Model):
    idshop = models.AutoField(db_column='idShop', primary_key=True)  # Field name made lowercase.
    idaddress = models.ForeignKey(Address, models.DO_NOTHING, db_column='idAddress', blank=True, null=True)  # Field name made lowercase.
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Shop'


class Website(models.Model):
    idwebsite = models.AutoField(db_column='idWebsite', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
