# -*- coding: utf-8 -*-
from django.db import models


class ImgMaterial(models.Model):
    
    name = models.CharField(u'文件名', max_length=256)
    alias = models.CharField(u'实际保存的名字', max_length=255, unique=True)
    describe = models.TextField(u'描述', max_length=256, null=True, blank=True)
    old_path = models.CharField(u'图片处理前的路径', max_length=256)
    new_path = models.CharField(u'图片处理后的路径', max_length=256)
    create_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='创建人')
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    write_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='更新人')
    write_date = models.DateTimeField(u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'素材管理'
        verbose_name_plural = u'对上传的素材进行管理，包括图片原始上传路径，处理之后的位置'
        db_table = 'img_material'
