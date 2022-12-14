from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Questions(models.Model):
    title=models.CharField(max_length=300)
    descriptions=models.CharField(max_length=500)
    image=models.ImageField(upload_to="images",null=True)
    created_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        return self.title



class Answers(models.Model):
        questions=models.ForeignKey(Questions,on_delete=models.CASCADE)
        answer=models.CharField(max_length=200)
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        upvote=models.ManyToManyField(User,related_name='upvote')
        created_date=models.DateField(auto_now_add=True)


        def __str__(self):
            return self.answer
            
