from django.db import models

from markdownx.models import MarkdownxField
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Blog(models.Model):
    title = models.CharField('Title', max_length=50)
    text = MarkdownxField('Text')
    created_at = models.DateField('Create Date', auto_now_add=True)
    uppdated_at = models.DateField('Uppdate Date', auto_now = True)

    def get_text_markdownx(self):
        return mark_safe(markdownify(self.text))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blog'