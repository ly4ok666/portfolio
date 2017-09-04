from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField


class Article(models.Model):
    article_title = models.CharField(max_length=60, verbose_name='Заголовок')
    article_text = RichTextUploadingField(verbose_name='Текст статьи')
    # можно нафик убрать время или вообще всё
    article_date = models.DateTimeField(verbose_name="Дата и время")
    # можно убрать нафик
    article_likes = models.IntegerField(default=0)
    article_image = models.ImageField(null=True, blank=True, upload_to="images/",
                                      verbose_name=u'Изображение', )
    video = EmbedVideoField(null=True, blank=True, verbose_name=u'Видео', )


    def __str__(self):
        return self.article_text[:50] + "..."
    def __unicode__(self):
        return self.article_title
    def bit(self):
        if self.article_image:
            return u'<img src="%s" width="70"/>' % self.article_image.url
        else:
            return u'(none)'

    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True
    class Meta():
        db_table = "article"
        verbose_name = 'статьи'
        verbose_name_plural = 'статьи'
        ordering = ['-article_date']