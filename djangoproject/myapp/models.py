from django.db import models

# Create your models here.

# 고양이 게시판에 맞는 데이터베이스에 들어갈 내용을 설정해야함
# 제목 , 사진 ,  내용 이렇게 들어갈건데
# 내용 처음에 들어가면 나이 성별 위치 같은거 나타내주면 좋음
class PolicyList(models.Model):
    # 제목
    title = models.CharField(max_length=100)
    # 내용
    body = models.TextField()

    # 작성자 
    writer = models.CharField(max_length=20, default="admin")

    # 등록일 , auto_now = True 가 매번 저장될때마다 시간이 저장
    pub_date = models.DateTimeField(auto_now=True)

    # 조회수 - 미구현 기본 = 0
    hits = models.IntegerField(default=0)
    
    # 첨부파일 - 미구현
    #upload_file = models.FileField()

    def hits_counter(self):
        self.hits += 1
        self.save()
        return self.hits

    def __str__(self):
        return self.title
