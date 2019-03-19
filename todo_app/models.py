from django.db import models
from django.utils import timezone

# Create your models here.




STATUS = (
    ('In Progress', 'In Progress'),
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),

)

class Todo(models.Model):
	title = models.CharField(max_length=250) 
	description = models.TextField(blank=True) 
	status = models.CharField(choices=STATUS, max_length=50,blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	task_date = models.DateTimeField()
	is_delete = models.NullBooleanField(default=False)

	class Meta:
		ordering = ["-created_at"] 

	def __str__(self):
		return self.title 
