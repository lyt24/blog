from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # 正整数字段
    object_id = models.PositiveIntegerField()
    # 泛型外键，其实是用复合数据实现，一个值表示外键model类型，一个表示外键值
    content_object = GenericForeignKey('content_type', 'object_id')


# 没有继承任何模型
class ReadNumExpandMethod:
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0


class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now)
    read_num = models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # GenericForeignKey可以通过 content_object 访问具体的模型
    content_object = GenericForeignKey('content_type', 'object_id')
