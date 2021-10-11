from django.db import models
from django.shortcuts import reverse
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class SubjectNames(models.Model):
    subject_name = models.CharField(max_length=300)
    subject_description = models.TextField()

    def __str__(self):
        return self.subject_name

    def get_absolute_url(self):
        return reverse("uroki", kwargs={"subject_id": self.pk})

    def return_subject_id_for_create_urok(self):
        return reverse("create_urok", kwargs={"subject_id": self.pk})


class Uroki(models.Model):
    # db_index означает, что поиск по этому полю будет быстрее. необязательный параметр
    urok_name = models.CharField(max_length=300, db_index=True)
    urok_description = models.CharField(max_length=1000)
    urok_text = models.TextField()
    subject = models.ForeignKey(SubjectNames, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.urok_name

    def return_subject_id(self):
        return reverse("uroki", {"pk": self.pk})



    # def get_absolute_url(self):
    #     return reverse("uroki", kwargs={"urok_id": self.pk})
