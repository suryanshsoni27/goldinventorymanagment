from django.db import models

# Create your models here.


class jewellery(models.Model):
    type = models.CharField(max_length=100, blank=False)  # name of column
    price = models.IntegerField()
    choice = (('AVAILABLE', 'Item ready to be sold'), ('SOLD',
                                                       'Item sold'), ('In production', 'Item in manufacturing'))  # drop down options
    status = models.CharField(
        max_length=100, choices=choice, default="not available")  # set up drop down options
    issues = models.CharField(max_length=100, default="no stuff")

    class Meta:
        abstract = True


def __str__(self):
    return 'Type: {0} Price: {1}'.format(self.type, self.price)


class earring(jewellery):
    pass


class rings(jewellery):
    pass


class diamonds(jewellery):
    pass


# this defines entire database
