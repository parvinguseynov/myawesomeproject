import datetime
from django.db import models
from django.utils import timezone

# Create your models here.



class Post(models.Model):
    post_title = models.CharField(max_length=300)
    post_date = models.DateTimeField()
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='posts_image/')

    # def __str__(self):
    #     return self.post_text


    # def was_published_recently(self):
    #     return self.post_date >= timezone.now() - datetime.timedelta(days=1)






