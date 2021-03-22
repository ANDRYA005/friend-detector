from django.db import models


class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.id})"

    class Meta:
        ordering = ["id"]
        verbose_name = "Person"
        verbose_name_plural = "People"
