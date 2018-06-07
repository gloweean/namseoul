from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def validate_max_chapter(value):
    if (value > 66) or (value < 1):
        raise ValidationError(_('%(value)s is over chapter range(1~66)'), params={'value': value})


class Bible(models.Model):
    def __str__(self):
        title = '{} {}장 {}절 - {}'.format(self.testament_kr_code, self.chapter, self.verse, self.contents)
        return title
    
    testament_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='성서 이름')
    testament_kr_code = models.CharField(max_length=50, blank=True, null=True, verbose_name='성서 약어')
    order = models.IntegerField(blank=True, null=True, validators=[validate_max_chapter], verbose_name='성서 번호')
    chapter = models.PositiveIntegerField(blank=True, null=True, verbose_name='장')
    verse = models.PositiveIntegerField(blank=True, null=True, verbose_name='절')
    contents = models.TextField(blank=True, null=True, verbose_name='본문')
    total_chapters = models.PositiveIntegerField(blank=True, null=True, verbose_name='성서의 장수')
    total_verses = models.PositiveIntegerField(blank=True, null=True, verbose_name='해당 장의 절수')
    version = models.CharField(max_length=100, default='개역개정', blank=True, null=True, verbose_name='개정종류')
    
    def save(self, *args, **kwargs):
        validate_max_chapter(self.order)
        models.Model.save(self, *args, **kwargs)
    
    class Meta:
        db_table = 'bible'
        verbose_name = 'bible'
        verbose_name_plural = verbose_name
