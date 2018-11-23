from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

GRADE = (('', '----'), ('1', '1'), ('2', '2'),
    ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'))

class S4HUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
            related_name="s4h_user")
    school_year = models.ForeignKey('school.schoolyear', on_delete=models.DO_NOTHING)

    def create_user(self):
        if not hasattr(self, "user"):
            self.user = User()

    def name(self, name):
        self.create_user()
        names = name.split()
        self.user.first_name = names.pop(0)
        self.user.last_name = str.join(" ", names)

    def full_name(self):
        self.create_user()
        name = str.join(" ", [self.user.first_name, self.user.last_name])
        return name

    def save(self, *args, **kwargs):
        self.user.save()
        self.user_id = self.user.pk
        super(S4HUser, self).save(*args, **kwargs)

    def __str__(self):
        return '\n'.join((self.full_name(), '<' + self.user.username + '>'))

class Validation():

    def hasNumbers(self, string):
        if (string is not None):
            if any(char.isdigit() for char in string):
                return True

            return False

        else:
            return False

    def hasSpecialCharacters(self, string):
        if (string is not None):
            for character in '@#$%^&+=/\{[]()}-_+=*!§|':
                if character in string:
                    return True

        return False
