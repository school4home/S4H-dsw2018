from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.
class Material(PolymorphicModel):

    class Meta:
        abstract = True

    def displayMaterial(self):
        pass

class Exercise(Material):
    """
    Define behavior for components having children.
    Store child components.
    Implement child-related operations in the Component interface.
    """
    name = models.CharField(max_length=50, null=False)
    start_date = models.DateField()
    close_date = models.DateField()
    description = models.CharField(max_length=500, null=False)
    Question = models.TextField(blank=True, null=True)

    def __init__(self):
        self._list_of_material = []

    def displayMaterial(self):
        for i in self._list_of_material:
            i.displayMaterial()

    def add(self, material):
        self._list_of_material.append(material)

    def remove(self, material):
        self._list_of_material.remove(material)