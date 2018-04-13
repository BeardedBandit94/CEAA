from django.db import models

# Create your models here.



class Application(models.Model):
    app_name = models.CharField(max_length=50)

    AVAILABLE = 'av'
    UNAVAILABLE = 'un'
    app_stat_choices = (
        (AVAILABLE, ' Available'),
        (UNAVAILABLE, 'Unavailable'),
    )

    app_stat = models.CharField(
        max_length=2,
        choices=app_stat_choices,
        default=AVAILABLE,

    )

    def status(self):
        if self.app_stat == 'av':
            return 'Available'
        elif self.app_stat == 'un':
            return 'Unavailable'

    def __str__(self):
        return self.app_name + ' - ' + self.status()
