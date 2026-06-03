from django.db import models

# Create your models here.
class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=20)


class Product(models.Model):
    pname = models.CharField(max_length=30)
    pprice = models.FloatField()
    cat = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)


    #for getting the product name in print statement globally
    def __str__(self):
        return self.pname
    
class Categories(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=20)

    def __str__(self):
        return self.cat_name


class Products(models.Model):
    pname = models.CharField(max_length=30)
    pprice = models.FloatField()
    cat = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)


    #for getting the product name in print statement globally
    def __str__(self):
        return self.pname