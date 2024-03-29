from django.db import models
from django.template import defaultfilters

# Create your models here.

class Series(models.Model):  
    STATE = [
        ('EM', 'En emisión'),
        ('TR', 'Terminado'),
        ('PR', 'Próximamente'),
    ]
    
    BANNER_STATE = [
        ('AC', 'Active'),
        ('DC', 'Deactivate')
    ]

    name = models.CharField(max_length=500, blank=False)

    picture = models.ImageField(upload_to='series/posts')
    picture_banner = models.ImageField(
        upload_to='series/banner', 
        blank=True, 
        null=True
    )

    banner_state = models.CharField(
        max_length=2,
        choices=BANNER_STATE,
        default='DC'    
    )

    state = models.CharField(
        max_length=12, 
        choices=STATE, 
        default='EM'
    )

    slug = models.SlugField(max_length=100)
    
    sinopsis = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Series, self).save(*args, **kwargs)

    def __str__(self):
        """Return name Serie"""
        return self.name


class Episodes(models.Model):
    serie = models.ForeignKey(Series, on_delete=models.CASCADE)

    name = models.CharField(max_length=500, blank=True, null=True) 
    episode = models.CharField(
        max_length=13, 
        default='Episodio 1', 
        blank=False,
        null=False
    )
    sinopsis = models.TextField(blank=True)

    URL_video = models.URLField(
        blank=False, 
        null=False, 
        default=''
    )
    
    slug = models.SlugField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Episodes, self).save(*args, **kwargs)

    def __str__(self):
        """Return Episode"""
        return self.episode