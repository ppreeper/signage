from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/beerthumbs/")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class ImageQueue(models.Model):
    name = models.CharField(max_length=200)
    images = models.ManyToManyField(Image)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Newsitem(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class NewsitemQueue(models.Model):
    name = models.CharField(max_length=200)
    newsitems = models.ManyToManyField(Newsitem)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Ticker(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class TickerQueue(models.Model):
    name = models.CharField(max_length=200)
    tickers = models.ManyToManyField(Ticker)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Screen(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    images = models.ManyToManyField(ImageQueue)
    newsitems = models.ManyToManyField(NewsitemQueue)
    tickers = models.ManyToManyField(TickerQueue)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
