from django.db import models
import uuid

# Create your models here.
class Task(models.Model) :
 title = models.CharField(max_length=200)
 completed = models.BooleanField(default=False)
 created = models.DateTimeField(auto_now_add = True)
 id = models.UUIDField(default=uuid.uuid4, unique=True, editable=True, primary_key=True)

 def __str__(self) :
  return self.title