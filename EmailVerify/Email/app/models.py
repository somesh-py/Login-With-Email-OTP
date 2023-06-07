from django.db import models

# Create your models here.

GENDER=(
    ('female','female'),
    ('male','male')
)

HOBBIES=(
    ('sports','sports'),
    ('gaming','gaming'),
    ('Study','Study'),
    ('reading','reading'),
    ('hiking','hiking'),
    ('travelling','travelling')
)

NATIONALITY=(
    ('India','India'),
    ('Out Of India','Out Of India'),
    ('Overseas','Overseas')
)

REGION=(
    ('Asia','Asia'),
    ('Europe','Europe'),
    ('Western','Western')    
)
class Registration(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=50)
    mobile=models.IntegerField(max_length=10)
    gender=models.CharField(choices=GENDER,max_length=50)
    hobbies=models.CharField(choices=HOBBIES,max_length=50)
    email=models.EmailField(max_length=254)
    nationality=models.CharField(choices=NATIONALITY,max_length=50)
    region=models.CharField(choices=REGION,max_length=50)
    image=models.ImageField(upload_to='Pimages')
    description=models.TextField()