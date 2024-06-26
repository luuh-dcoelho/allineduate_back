from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.constants import COUNTRY_CODES


class Clinic(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Nome'))
    title = models.CharField(max_length=255, default='Atendimento', verbose_name=_('Titulo'))
    address1 = models.CharField(max_length=255, verbose_name=_('Rua'))
    address2 = models.CharField(
        max_length=100, verbose_name=_('Bairro'))
    city = models.CharField(max_length=255, verbose_name=_('Cidade'))
    country_code = models.CharField(
        max_length=5, default='+55', choices=COUNTRY_CODES, verbose_name=_('Código do País'))
    maps_link = models.URLField()
    phone = models.CharField(max_length=20, verbose_name=_('Telefone'))
    plans = models.ManyToManyField(
        'Plan', related_name='clinics', verbose_name=_('Planos'))

    class Meta:
        verbose_name = _('Clínica')
        verbose_name_plural = _('Clínicas')

    def __str__(self):
        return self.name


class ClinicHours(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE,
                               related_name='clinic_hours', verbose_name=_('Clínica'))
    day_of_week = models.IntegerField(choices=[
        (0, _('Segunda Feira')),
        (1, _('Terça Feira')),
        (2, _('Quarta Feira')),
        (3, _('Quinta Feira')),
        (4, _('Sexta Feira')),
        (5, _('Sábado')),
        (6, _('Domingo')),
    ], verbose_name=_('Dia da Semana'))
    opening_time = models.TimeField(verbose_name=_('Hora de Abertura'))
    closing_time = models.TimeField(verbose_name=_('Hora de Fechamento'))

    class Meta:
        verbose_name = _('Horário da Clínica')
        verbose_name_plural = _('Horários das Clínicas')

    def __str__(self):
        return f'{self.day_of_week} - {self.clinic.name}'


class Plan(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Nome'))
    duration = models.DurationField(
        default=timedelta(hours=1), verbose_name=_('Duração'))

    class Meta:
        verbose_name = _('Plano')
        verbose_name_plural = _('Planos')

    def __str__(self):
        return self.name
