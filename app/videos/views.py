from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from rest_framework.exceptions import NotFound
from rest_framework import status

# 1.VideoList
# api/v1/videos
# - GET: 전체 비디오 목록 조회 => Video.objects.all() => 클라이언트에 전달
# - POST: 새로운 비디오 생성
# - DELETE, PUT: X
class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all()
        print('videos : ', videos) # 직렬화 (장고객체->JSON으로 변환) => SERIALRIZER

        serializer = VideoSerializer(videos, many=True) # 쿼리셋이 2개 이상

        return Response(serializer.data)
    
    def post(self, request):
        try:
            user_data = request.data # json -> 파이썬이 이해할 수 있나요? -> Serializer
            serializer = VideoSerializer(data=user_data)
            
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

        except Exception as e:
            return Response({'msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 2.VideoDetail
# api/v1/videos/{video_id}
# - GET: 특정 비디오 상세 조회
# - POST: X
# - PUT: 특정 비디오 정보 업데이트(수정)
# - DELETE: 특정 비디오 삭제
class VideoDetail(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound

    def get(self, request, pk): # pk: Primary Key(ID)
        video = self.get_object(pk)
        serializer = VideoSerializer(video)

        return Response(serializer.data)
    
    def put(self, request, pk):
        video = self.get_object(pk)
        user_data = request.data

        try:
            serializer = VideoSerializer(video, data=user_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        except Exception as e:
            return Response({'msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)