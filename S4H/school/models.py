from django.db import models

class SchoolYear(models.Model):
    year = models.DecimalField(max_digits=1,decimal_places=0)

    @staticmethod
    def get_instance(desired_year):
        return SchoolYear.objects.get(year=desired_year)

    def __str__(self):
        return str(self.year) + ' ano'
