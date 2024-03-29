from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

class Notification(CommonModel):
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)

    # User:Notification => 1:N , N:N, 1:1 
    # Video:Notification => 1:N