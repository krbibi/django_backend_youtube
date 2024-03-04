from rest_framework.views import APIView
from .models import Reaction
from .serializer import ReactionSerializer
from rest_framework.response import Response
from rest_framework import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST
)

class ReactionAPIView(APIView):
    # 좋아요, 싫어요 생성 or 업데이트 
    def pose(self,request,video_id):
        user_data = request.data # 유저가 서버로 보낸 데이터
        serializer = ReactionSerializer(data = user_data)


        if serializer.is_valid():
            print('serializer.validated_data : ', serializer.validated_data)
            
            reaction_obj, created = Reaction.objects.get_or_create(
                user=request.user,
                video=video_id,
                defaults={'reaction': user_data['reaction']}
            )
            
            # created : boolean (True : 새로생성, False: 기존 객체가 존재한다.)
            if created:
                return Response(serializer.data, status=HTTP_201_CREATED)
            
            #기존 데이터가 존재한느 경우 -> UPDATE
            if not created:
                reaction_obj.reaction = serializer.validated_data['reaction']
                reaction_obj.save()

                return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)