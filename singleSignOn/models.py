from django.db import models

# Create your models here.
#class IDLUsers(models.Model) :
#    userid = models.IntegerField()
#    ssoaccount = models.CharField(max_length = 255)
#    usernickname = models.CharField(max_length = 255)
#    createdate = models.DateTimeField()
#    lastlogin = models.DateTimeField(blank = True)
#
class Idlusers(models.Model):
    userid = models.AutoField(primary_key=True)
    ssoaccount = models.CharField(max_length=255)
    usernickname = models.CharField(max_length=255)
    createdate = models.DateTimeField(blank=True, null=True)
    lastlogon = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idlusers'
    
