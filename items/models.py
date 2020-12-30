from django.db import models  

class Item(models.Model):  
    eid = models.IntegerField()
    etype = models.CharField(max_length=100)
    etitle = models.CharField(max_length=100)
    eauthor = models.CharField(max_length=100)  
    estatus = models.CharField(max_length=20)  
    class Meta:  
	    db_table = "Item"