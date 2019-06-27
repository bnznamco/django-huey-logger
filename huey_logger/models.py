from django.db import models


class LastCronRun(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(auto_now=True)


class CronError(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    error = models.TextField()
