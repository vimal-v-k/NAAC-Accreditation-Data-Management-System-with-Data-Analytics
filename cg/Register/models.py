from django.db import models


class rDetails(models.Model):
    RName = models.CharField(max_length=50)
    REmail = models.CharField(max_length=50)
    RPassword = models.CharField(max_length=100)
    RConfirm_password = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.RName