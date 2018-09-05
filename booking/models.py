from django.db import models


class Car(models.Model):
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_registration = models.CharField(max_length=50)
    car_vin = models.CharField(max_length=50)


    # h1_tag = models.CharField(max_length=50, null=True, blank=True)
    # description = models.TextField(max_length=500, null=True, blank=True)
    # slug = models.SlugField(unique=True)
    # seo_title = models.CharField(max_length=100, null=True, blank=True)
    # seo_description = models.CharField(max_length=200, null=True, blank=True)
    # seo_primary_keyword = models.CharField(max_length=50, null=True, blank=True)
    # seo_secondary_keyword = models.CharField(max_length=50, null=True, blank=True)
    # twitter_account = models.CharField(max_length=15, null=True, blank=True) #todo change the field type
    # twitter_tag = models.CharField(max_length=15, null=True, blank=True) #todo change the field type
    # facebook_page = models.CharField(max_length=15, null=True, blank=True)  # todo change the field type
    # facebook_group = models.CharField(max_length=15, null=True, blank=True)  # todo change the field type

    def __str__(self):
        return self.car_registration