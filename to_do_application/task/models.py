from django.db import models

from datetime import date

# Create your models here.
PRIORITY_CHOICES = ( 
    (1, 'Low'), 
    (2, 'Normal'), 
    (3, 'High'), 
) 

STATE_CHOICES = ( 
    (1, 'Todo'), 
    (2, 'Doing'), 
    (3, 'Done'), 
) 

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=2500)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    state_of_task = models.IntegerField(choices=STATE_CHOICES)
    due_date = models.DateField()
    
    def __str__(self):
        return self.name

    @property
    def is_past_due(self):
        return date.today() > self.due_date

    class Meta: 
        ordering = ['-priority', 'name'] 
    class Admin: 
        pass
