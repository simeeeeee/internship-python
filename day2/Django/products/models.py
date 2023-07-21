from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)  #이름
    location = models.CharField(max_length=60)  #위치
    active = models.BooleanField(default=True)  ##만약 DB에 데이터 넣은 후 변경사항이 생겼을땐 이전에 만든 부분 처리할때 default사용

    def __str__(self): 
        return self.name  ##object에 대해서 object의 이름을 name으로 하라는 의미

class Book(models.Model):  #Book product
    author = models.ForeignKey(Author, 
                               on_delete=models.CASCADE,
                               related_name="books")
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=120)
    price = models.IntegerField()
    shipping_cost = models.IntegerField()
    quantity = models.PositiveIntegerField()  ##PositiveIntegerField() -> 양수 only

    def __str__(self):
        return f"{self.name} by {self.author.name}"
    
    