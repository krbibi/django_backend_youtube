from django.db import models

class CommonModel(models.Model):
    # 데이터가 생성된 시간
    created_at = models.DateTimeField(auto_now_add=True)

    # 데이터가 업데이트된 시간 => 업데이트된 시간으로 최신화가 이뤄져아함.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # DB테이블에 추가하지 마라