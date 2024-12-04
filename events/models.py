from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()

    featured = models.BooleanField(default=False)
    participants = models.ManyToManyField('members.Member', related_name='events')
    location = models.ForeignKey("facilities.Facility", on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.name