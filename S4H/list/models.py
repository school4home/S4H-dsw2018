from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib import messages

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


class TextQuestion(Material):
    """
    Represent leaf objects in the composition. A leaf has no children.
    Define behavior for primitive objects in the composition.
    """
    name = models.CharField(max_length=50, null=False)
    start_date = models.DateField()
    close_date = models.DateField()
    description = models.CharField(max_length=500, null=False)
    text = models.TextField(blank=True, null=True)

    def displayMaterial(self):
        return self.text


class VideoQuestion(Material):
    """
    Represent leaf objects in the composition. A leaf has no children.
    Define behavior for primitive objects in the composition.
    """
    name = models.CharField(max_length=50, null=False)
    start_date = models.DateField()
    close_date = models.DateField()
    description = models.CharField(max_length=500, null=False)
    video = models.TextField(blank=True, null=True)

    def displayMaterial(self):
        return self.video


class ImageQuestion(Material):
    """
    Represent leaf objects in the composition. A leaf has no children.
    Define behavior for primitive objects in the composition.
    """
    name = models.CharField(max_length=50, null=False)
    start_date = models.DateField()
    close_date = models.DateField()
    description = models.CharField(max_length=500, null=False)
    photo = models.ImageField(upload_to='photoQuestion')

    def displayMaterial(self):
        return self.photo

class GradeObserver(models.Model):
    """
    Represents the grade observer who watches for a new grade and notifies
    the specified user
    """
    MESSAGE_1 = 'Voce recebeu uma nova nota! O seu valor e '
    CONGRATS = 'Parabens!'
    STUDY = 'Vamos revisar!'
    message = models.CharField(max_length=500, default='')
    message_type = models.DecimalField(max_digits=5,decimal_places=0,
        default=messages.SUCCESS,blank=messages.SUCCESS,null=messages.SUCCESS)

    def update(self, grade):
        grade_value = grade.value
        if grade_value > 7:
            new_message = self.MESSAGE_1 + str(grade_value) + '. ' + self.CONGRATS
            self.message_type = messages.SUCCESS
        else:
            new_message = self.MESSAGE_1 + str(grade_value) + '. ' + self.STUDY
            self.message_type = messages.WARNING
        self.message = new_message
        super(GradeObserver, self).save()

    def clear(self):
        self.message = ''
        super(GradeObserver, self).save()

class Grade(models.Model):
    """
    Represents the grade ie school year in which the student is in.
    """
    value = models.DecimalField(max_digits=2, decimal_places=0)
    student = models.ForeignKey('user.S4HUser', on_delete=models.CASCADE)
    grade_observer = models.ForeignKey(GradeObserver, on_delete=models.CASCADE)

    def notify_grade(self):
        self.grade_observer.update(self)

    def save(self, *args, **kwargs):
        self.notify_grade()
        super(Grade, self).save(*args, **kwargs)
