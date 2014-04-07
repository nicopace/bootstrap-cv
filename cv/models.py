from django.db import models

# Create your models here.

class Curriculum(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    cool_line = models.CharField(max_length=255)

    profile = models.CharField(max_length=2000)
    
    education_text = models.CharField(max_length=2000)
    degrees = models.ManyToManyField(Degree)

    trainings = models.ManyToManyField(Training)
    
    certificates = models.ManyToManyField(Certificate)

    works = models.ManyToManyField(Work)

    skills = models.ManyToManyField(Skill)

    extra = models.CharField(max_length=2000)

    blogposts = models.ManyToManyField(Blogpost)

    contributions = models.ManyToManyField(Contribution)

    testimonials = models.ManyToManyField(Testimony)
    
    # Contact Info

    address = models.CharField()
    city = models.CharField()
    country = models.CharField()
    postal_code = models.CharField()
    mobile_phone = models.CharField()
    email = models.EMailField()


class Degree(models.Model):
    degree = models.CharField(max_length=50)
    progress = models.IntegerField(default=0)
    year = models.DateField()
    institute = models.CharField(max_length=100)


class Training(models.Model):
    skill = models.CharField(max_length=50)
    stars_number = models.IntegerField(default=0)
    date = models.DateField()
    institute = models.CharField(max_length=100)


class Certificate(models.Model):
    skill = models.CharField(max_length=50)
    stars_number = models.IntegerField(default=0)
    date = models.DateField()
    institute = models.CharField(max_length=100)


class Work(models.Model):
    title = models.CharField(max_length=50)
    current = model.BooleanField()
    description = model.CharField(max_length=2000)


class Skill(models.Model):
    value = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

class WorkSkill(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = URLField()
    related_skill = models.ForeignKey('Skill')


class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    image_url= models.URLField()
    date = models.DateField()
    summary = models.CharField(max_length=2000)
    url = models.URLField()


class Contribution(models.Model):
    name = models.CharField()
    technologies = models.ManyToManyField('Technology')
    description = models.CharField(max_length=2000)
    url = models.URLField()


class Technology(models.Model):
    name = models.CharField()


class Testimony(models.Model):
    image_url = models.URLField()
    name = models.CharField()
    role = models.CharField()
    company = models.CharField()
    content = models.CharField()

