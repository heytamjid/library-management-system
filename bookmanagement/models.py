from django.db import models
from django.contrib.auth.models import User



class Category (models.Model):
    categroyid =  models.AutoField(primary_key=True) 
    categoryname = models.CharField( max_length=100)
    
    def __str__ (self):
        return f"Category: {self.categoryname}" 
    
#

class Book (models.Model):
    bookid =  models.AutoField(primary_key=True) 
    bookname = models.CharField(max_length=100, unique = False)
    author = models.CharField(max_length=100, unique = False)
    isbn = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    #price = models.IntegerField()
    stock = models.IntegerField()
    isAvaiable = models.BooleanField(default=True)
    cat = models.ManyToManyField(Category, blank=True, related_name='catRelated' )
    borrowedby = models.ManyToManyField(User, blank=True, related_name='borrowedbyRelated')
    publication_date  = models.DateTimeField()
    #modified_date = models.DateTimeField(auto_now = True)
    #review = models.ManyToManyField(Review, blank=True, related_name='reviewRelated')
    image = models.ImageField( upload_to='bookcovers/', blank=True)
    wishlist = models.ManyToManyField(User, blank=True, related_name='wishlistRelated')
    page = models.IntegerField()


    def __str__ (self):
        return f"Book: {self.bookname}" 
    

class Review (models.Model):
    reviewid =  models.AutoField(primary_key=True) 
    reviewString = models.CharField(max_length=500)
    reviewGivenBy = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewOnBook = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__ (self): 
        return f"ReviewID: {self.reviewid}" 


