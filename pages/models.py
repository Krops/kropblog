from django.db import models


class Pages(models.Model):
    slug = models.SlugField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True, auto_created=True)
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.slug

    def get_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def get_summary(self):
        return self.body[:30]
