from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from .models import Video
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

import pdb # 미션: pdb를 사용해서 아래의 테스트 코드를 디버깅하시오.

class VideoAPITestCase(APITestCase):
    # 테스트 코드가 실행되기 전 (1) 유저 생성 (2) 비디오 생성
    def setUp(self):
        # 유저 생성
        self.user = User.objects.create_user(
            email='sy@gmail.com',
            password='password123'
        )
        self.client.login(email='sy@gmail.com', password='password123')

        # 비디오 생성
        self.video = Video.objects.create(
            title='test video',
            link='http://test.com',
            user=self.user
        )

    def test_video_list_get(self):
        url = reverse('video-list')
        print('url', url)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_video_detail_get(self):
        # kwargs: keyword arguments
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        res = self.client.get(url) # api/v1/videods/1

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # 비디오가 잘 생성되는지 확인해보기 위한 테스트
    def test_video_list_post(self):
        url = reverse('video-list')

        data = {
            'title': 'test video2',
            'link': 'http://test.com',
            'category': 'test category',
            'thumbnail': 'http://test.com',
            'video_uploded_url': 'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b"file_content", content_type='video/mp4'),
            'user': self.user.pk # 1
        }

        res = self.client.post(url, data)
        # pdb.set_trace()
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    # 비디오 정보 업데이트
    def test_video_detail_put(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})

        data = {
            'title': 'updated video',
            'link': 'http://test.com',
            'category': 'test category',
            'thumbnail': 'http://test.com',
            'video_uploded_url': 'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b"file_content", content_type='video/mp4'),
            'user': self.user.pk # 1
        }

        res = self.client.put(url, data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], 'updated video')

    # 비디오 삭제
    def test_video_detail_delete(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        # 정말 데이터가 정상적으로 삭제 되었는가?
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)