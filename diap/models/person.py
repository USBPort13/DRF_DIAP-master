from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.urls import reverse

from diap.models.choices import PersonTypeSocialNetworkChoices


class Person(models.Model):
    class StatusPersonPostChoices(models.TextChoices):
        DELETED = 'DELETED', _('Deleted')
        PUBLISHED = 'PUBLISHED', _('Published')
        PROCESSING = 'PROCESSING', _('Processing')

    class StatusPersonChoices(models.TextChoices):
        ALIVE = 'ALIVE', _('Alive')
        CAPTIVITY = 'CAPTIVITY', _('Captivity')
        DIE = 'DIE', _('Die')
        MISSING_PERSON = 'MISSING_PERSON', _('Missing person')

    # -- Main information about Person -- #
    first_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='Прізвище')
    middle_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='Побатькові')
    birthday = models.DateField(blank=True, null=True, verbose_name='Дата народження')
    citizenship = models.CharField(max_length=64, blank=True, null=True, verbose_name='Громадянство')
    passport = models.CharField(max_length=64, blank=True, null=True, verbose_name='Паспорт')
    individual_identification_number = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        verbose_name='Індитифікаційний код'
    )
    place_of_birthday = models.CharField(max_length=128, blank=True, null=True, verbose_name='Місце народження')
    place_of_living = models.CharField(max_length=128, blank=True, null=True, verbose_name='Місце проживання')

    # -- Military Person fields -- #
    range = models.CharField(max_length=64, blank=True, null=True, verbose_name='Військове звання')
    job_title = models.CharField(max_length=128, blank=True, null=True, verbose_name='Посада')
    military_unit = models.CharField(max_length=256, blank=True, null=True, verbose_name='Військова частина')
    type_of_army = models.CharField(max_length=128, blank=True, null=True, verbose_name='Рід військ')
    military_from = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        verbose_name='Місце знаходження військової частини'
    )

    # -- Person status & what's happends
    status_person = models.CharField(
        max_length=32,
        choices=StatusPersonChoices.choices,
        default=StatusPersonChoices.DIE,
        verbose_name='Статус'
    )
    place_where_accident = models.CharField(max_length=64, blank=True, null=True, verbose_name='Місце інцидету')
    data_when_accident = models.DateField(default=None, blank=True, null=True, verbose_name='Дата інциденту')

    # -- Date log -- #
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час останьої зміни')

    # -- Post status -- #
    post_status = models.CharField(
        max_length=32,
        choices=StatusPersonPostChoices.choices,
        default=StatusPersonPostChoices.PROCESSING,
        verbose_name='Статус поста'
    )

    # -- User -- #
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, null=True)

    # -- Absolute url Method -- #
    def get_absolute_url(self):
        return reverse('person', kwargs={'person_id': self.pk})

    def __str__(self):
        fild_name = self.last_name + ' ' + self.first_name + ' ' + self.middle_name
        return fild_name


class PersonImage(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d")
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='images')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        fild_name = 'Image: ' + self.person.last_name + ' ' + self.person.first_name + ' ' + self.person.middle_name
        return fild_name


class PersonText(models.Model):
    text_url = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Посилання на текст')
    text_from = models.CharField(max_length=128, verbose_name='Звідки текст (Домен)')
    text = models.CharField(max_length=8192, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час останьої зміни')

    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='texts')

    def __str__(self):
        fild_name = 'Text: ' + self.person.last_name + ' ' + self.person.first_name + ' ' + self.person.middle_name
        return fild_name


class PersonPlaceWhereHeWas(models.Model):
    place = models.CharField(max_length=128, verbose_name='Місця дислокації')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час останьої зміни')

    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='place_where_he_waa')

    def __str__(self):
        fild_name = 'Text: ' + self.person.last_name + ' ' + self.person.first_name + ' ' + self.person.middle_name
        return fild_name


class PersonSocialNetwork(models.Model):
    type = models.ForeignKey(PersonTypeSocialNetworkChoices, on_delete=models.CASCADE, verbose_name='Тип')
    profile = models.CharField(max_length=128, verbose_name='Посилання на профіль')
    profile_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='Логін профілю')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час останьої зміни')

    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='social_network')

