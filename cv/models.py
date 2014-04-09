from django.db import models

# Create your models here.


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
    current = models.BooleanField()
    description = models.CharField(max_length=2000)


class WorkSkill(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = models.URLField()
    related_skill = models.ForeignKey('Skill', related_name="works")


class Skill(models.Model):
    value = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)


class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    image_url= models.URLField()
    date = models.DateField()
    summary = models.CharField(max_length=2000)
    url = models.URLField()


class Contribution(models.Model):
    name = models.CharField(max_length=50)
    technologies = models.ManyToManyField('Technology')
    description = models.CharField(max_length=2000)
    url = models.URLField()


class Technology(models.Model):
    name = models.CharField(max_length=50)


class Testimony(models.Model):
    image_url = models.URLField()
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    content = models.CharField(max_length=50)


class Curriculum(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    cool_line = models.CharField(max_length=255, blank=True)

    profile = models.CharField(max_length=2000, blank=True)
    
    education_text = models.CharField(max_length=2000, blank=True)
    degrees = models.ManyToManyField(Degree, blank=True)

    trainings = models.ManyToManyField(Training, blank=True)
    
    certificates = models.ManyToManyField(Certificate, blank=True)

    works = models.ManyToManyField(Work, blank=True)

    skills = models.ManyToManyField(Skill, blank=True)

    extra = models.CharField(max_length=2000, blank=True)

    blogposts = models.ManyToManyField(Blogpost, blank=True)

    contributions = models.ManyToManyField(Contribution, blank=True)

    testimonials = models.ManyToManyField(Testimony, blank=True)
    
    # Contact Info

    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)
    mobile_phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
