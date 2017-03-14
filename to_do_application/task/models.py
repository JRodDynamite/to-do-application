from django.db import models

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
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=2500)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    state_of_task = models.IntegerField(choices=STATE_CHOICES)
    due_date = models.DateField()
    
    def __str__(self): 
        return self.name 
    class Meta: 
        ordering = ['-priority', 'name'] 
    class Admin: 
        pass
