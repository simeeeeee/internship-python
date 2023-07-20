from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)  #이름
    location = models.CharField(max_length=60)  #위치
    active = models.BooleanField(default=True)

    def __str__(self): 
        return self.name

class Book(models.Model):  #Book product
    author = models.ForeignKey(Author, 
                               on_delete=models.CASCADE,
                               related_name="books")
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=120)
    price = models.IntegerField()
    shipping_cost = models.IntegerField()
    quantity = models.PositiveIntegerField()  ##PositiveIntegerField() -> 양수 only