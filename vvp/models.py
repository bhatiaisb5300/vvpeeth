from django.db import models
# Create your models here.
class alumni(models.Model):

    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=15)
    Batch = models.CharField(max_length=5)
    Photo = models.FileField(upload_to='alumni/')
    address = models.CharField(max_length=100)
    date_time = models.CharField(max_length=100)

    def __str__(self):
        return self.First_name + self.Last_name


class our_gems(models.Model):

    Name = models.CharField(max_length=50)
    Marks = models.CharField(max_length=20)
    Photo = models.FileField(upload_to='our_gems/')
    Batch = models.CharField(max_length=5)
    Class = models.CharField(max_length=10)

    def __str__(self):
        return self.Name


class gallery(models.Model):

    Photo = models.FileField(upload_to='gallery/')
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=1000)

    def __str__(self):
        return self.Title

class notice_events(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    Photo = models.ImageField(upload_to='n_e/img')
    File = models.FileField(upload_to='n_e/docs',null=True,blank=True)
    Title = models.CharField(max_length=30)
    Description = models.CharField(max_length=1000)

    def __str__(self):
        return self.Title + str(self.date)


class staff(models.Model):

    s_no = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class committee(models.Model):

    s_no = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name
