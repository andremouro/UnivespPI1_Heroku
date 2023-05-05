from django.db import models

class File(models.Model):
    id = models.AutoField(primary_key=True, max_length=6)
    subject = models.CharField(max_length=15)
    school = models.CharField(max_length=15)
    sex = models.CharField(max_length=2)
    age = models.IntegerField(max_length=15)
    adress = models.CharField(max_length=15)
    famsize = models.CharField(max_length=15)
    Pstatus = models.CharField(max_length=2)
    Medu = models.IntegerField(max_length=15)
    Fedu = models.IntegerField(max_length=15)
    guardian = models.CharField(max_length=15)
    traveltime = models.IntegerField(max_length=15)
    studytime = models.IntegerField(max_length=15)
    failures = models.IntegerField(max_length=15)
    schoolsup = models.CharField(max_length=15)
    famsup = models.CharField(max_length=15)
    paid = models.CharField(max_length=15)
    activities = models.CharField(max_length=15)
    internet = models.CharField(max_length=15)
    famrel = models.IntegerField(max_length=15)
    freetime = models.IntegerField(max_length=15)
    goout = models.IntegerField(max_length=15)
    Dalc = models.IntegerField(max_length=15)
    health = models.IntegerField(max_length=15)
    absences = models.IntegerField(max_length=15)
    G1 = models.IntegerField(max_length=15)
    G2 = models.IntegerField(max_length=15)
    G3 = models.IntegerField(max_length=15)
    def __int__(self):	##Esta linha fará com que as entradas de dados no nosso banco de dados sejam apresentadas pelo 'id'
        return self.id

