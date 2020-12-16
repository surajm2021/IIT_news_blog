from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.urls import reverse
from django.conf import settings


class My_Blog(models.Model):
    title = models.CharField(max_length=100, help_text='Title of blog')
    description = models.TextField(help_text='Description of blog')
    date = models.DateTimeField(default=timezone.now)
    time = models.TimeField(default=now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 100 or img.width > 100:
    #         output_size = (500, 500)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})