from django.db import models

class Person(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"


# class StagedPerson(models.Model):

#     person = models.OneToOneField(Person, null=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.person.name
    
#     class Meta:
#         verbose_name = "Staged Person"
#         verbose_name_plural = "Staged Person"