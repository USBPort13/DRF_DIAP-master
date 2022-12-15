from django.db import models


class PersonTypeSocialNetworkChoices(models.Model):
    type = models.CharField(max_length=32, verbose_name='Тип')

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type

