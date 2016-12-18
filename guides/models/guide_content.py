# -*- coding: utf-8 -*-

from django.db import models


class Guidebody(models.Model):
    uuid = models.CharField('uuid', max_length=256)
    title = models.ForeignKey(u'guides.GuideTitle',verbose_name=u'文章标题id')
    s_title = models.CharField(u'段落标题', max_length=256, null=True)
    s_body = models.TextField(u'段落正文', null=True)
    image_path = models.CharField(u'图片路径', max_length=256, null=True)
    image_name = models.CharField(u'图片名称', max_length=256, null=True)
    image_msg=models.CharField(u'图片说明',max_length=256,null=True)
    image_location=models.CharField(u'位置',max_length=256,null=True)

    image_explain = models.TextField(u'图片描述正文', null=True)
    numbers=models.CharField(u'文章序号',max_length=256,null=True)
    parent = models.IntegerField(u'上一条记录',null=True)

    create_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='创建人')
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    write_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='更新人')
    write_date = models.DateTimeField(u'更新时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文档详细信息'
        verbose_name_plural = '文档标题及详细信息'
        db_table = 'guide_document_body'
