from typing import Iterable
from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.URLField()
    release_date = models.DateField(auto_created=False)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length = 200, unique=True, blank=True)
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    
