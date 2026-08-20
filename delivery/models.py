from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length= 20)
    password =models.CharField(max_length= 20)
    email = models.CharField(max_length= 20)
    mobile = models.CharField(max_length= 10)
    address = models.CharField(max_length= 50)

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    picture = models.URLField(max_length=200, default='https://www.google.com/imgres?q=restaurant%20hyderabad&imgurl=https%3A%2F%2Fwww.cathaypacific.com%2Fcontent%2Fdam%2Ffocal-point%2Fcx%2Finspiration%2F2025%2F01%2FThe_best_restaurants_and_bars_in_Hyderabad-Roast_CCx_Exterior-courtesyimages-1.renditionimage.900.900.jpg&imgrefurl=https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fen_IN%2Finspiration%2Fdining%2Fhyderabad-dining-guide.html&docid=fVY6uQwC9i-8wM&tbnid=7brpRxbrJ5w0iM&vet=12ahUKEwiBxs2B46mWAxUcUGwGHRBaDREQnPAOegUI_AEQAA..i&w=900&h=900&hcb=2&ved=2ahUKEwiBxs2B46mWAxUcUGwGHRBaDREQnPAOegUI_AEQAA')
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()