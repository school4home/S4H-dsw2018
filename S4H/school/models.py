from django.db import models

class SchoolYear(models.Model):
    year = models.DecimalField(max_digits=1,decimal_places=0)

    @staticmethod
    def get_instance(desired_year):
        return SchoolYear.objects.get(year=desired_year)

    def __str__(self):
        return str(self.year) + ' ano'

class Module(models.Model):
    name = models.CharField(max_length=200)
    year = models.ManyToManyField(SchoolYear, related_name='modules')

    @staticmethod
    def get_instance(module_name, school_year):
        return Module.objects.get(name=module_name, year=school_year)
