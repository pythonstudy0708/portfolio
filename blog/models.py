from django.db import models

# Create your models here.
# Create a blog models
class Blog(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    tagline = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

# Add the blog app to the settings

#create sa migration

#migrate

#add to the admin
