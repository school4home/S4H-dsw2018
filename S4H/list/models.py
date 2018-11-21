from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.
class Material(PolymorphicModel):

    class Meta:
        abstract = True

    def displayMaterial(self):
        pass
