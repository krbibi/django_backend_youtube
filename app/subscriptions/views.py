from rest_framework.views import APIView
from .serializers import SubscriptionSerializer
from rest_framework import status
from rest_framework.response import Response
# api/v1/subscriptions
# SubscriptionList
# [POST]: 구독하기 버튼 클릭
class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data
        serializer = SubscriptionSerializer(data=user_data) # json -> Object        
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


# api/v1/subscriptions/{user_id}
# SubscriptionDetail
# [DELETE]: 구독취소
from django.shortcuts import get_object_or_404
from .models import Subscription
class SubscriptionDetail(APIView):
    def delete(self, request, pk):
        subs = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        subs.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)