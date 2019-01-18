from django.db import models

# Create your models here.

class Business(models.Model):
    group = models.CharField(max_length=32)
    code = models.CharField(max_length=32,null=True,default='root')
class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(protocol='both',db_index=True)
    port = models.IntegerField()
    host_group = models.ForeignKey(to='Business',to_field='id',on_delete=models.CASCADE)

class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField(to='Host')
# class HostToApp(models.Model):
#     hid = models.ForeignKey(to='Host',to_field='nid',on_delete=models.CASCADE)
#     aid = models.ForeignKey(to='Application',to_field='id',on_delete=models.CASCADE)