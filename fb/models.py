from django.db import models


class FeedbackForm(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} wrote: \n{self.text}"
