from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(
        Employee, related_name="stores", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class Visit(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, related_name="visits", on_delete=models.CASCADE)
    latitude = models.FloatField()
    longtitude = models.FloatField()

    # def __str__(self) -> str:
    #     return super().__str__()
