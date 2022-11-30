from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    new_id = models.PositiveIntegerField()
    url = models.URLField()
    title = models.CharField(max_length=250, null=True)
    summary = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to="news/")
    date_published = models.DateTimeField(null=True)
    date_modified = models.DateTimeField(null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
