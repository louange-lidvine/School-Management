from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    member = models.ForeignKey('members.Member', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.facility.name} - {self.member.user.username}"