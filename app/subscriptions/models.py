from django.db import models
from common.models import CommonModel
from users.models import User

# User:Subscription => 1:N
class Subscription(CommonModel):
    # 나
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')

    # 내가 구독할 사람
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')