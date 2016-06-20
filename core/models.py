from django.db import models
from django.utils.translation import ugettext_lazy as _


class Line(models.Model):
    code_line = models.CharField(_('Code'), max_length=50)
    denomination = models.CharField(_('Name'), max_length=50)
    origin = models.CharField(
        _('Origin'), max_length=50, blank=True, null=True)
    line_return = models.CharField(
        _('Return'), max_length=50,  blank=True, null=True)
    circle = models.BooleanField(_('Circle'), default=False)

    created_at = models.DateTimeField(
        _('Created at'), auto_now_add=True, blank=True, null=True)
    changed_at = models.DateTimeField(
        _('Changed at'), auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        get_latest_by = "-created_at"

    def __str__(self):
        return "%s - %s" % (self.code_line, self.denomination)


class Stop(models.Model):
    code_stop = models.CharField(_('Code'), max_length=50)
    denomination = models.CharField(_('Denomination'), max_length=50)
    lat = models.CharField(
        _('Latitude'), max_length=50, blank=True, null=True)
    lon = models.CharField(
        _('Longitude'), max_length=50, blank=True, null=True)
    address = models.CharField(
        _('Address'), max_length=140, blank=True, null=True)

    created_at = models.DateTimeField(
        _('Created at'), auto_now_add=True, blank=True, null=True)
    changed_at = models.DateTimeField(
        _('Changed at'), auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        get_latest_by = "-created_at"

    def __str__(self):
        return self.denomination
