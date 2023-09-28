from django.db import models


class Post(models.Model):  # models.Model을 상속
    title = models.CharField(max_length=100)  # 제목 필드는 길이 제한이 있는 문자열로 저장 할거기 때문
    content = models.TextField()  # 내용필드는 길이 제한이 없는 문자열로 저장할 것이기 때문
