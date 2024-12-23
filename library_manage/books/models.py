from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.utils import timezone
from categories.models import Category




class Book(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='uploads/',blank = True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title



    

class Comment(models.Model):
    car = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.car.title}'
    
class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} borrowed {self.book.title}'

