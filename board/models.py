from django.db import models
from datetime import datetime

# Create your models here.
# on_delete : CASCADE, DO_NOTHING
from member.models import Member


class Board(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    member=models.ForeignKey(Member, related_name='board',
                             on_delete=models.CASCADE)
    # 왜래키 설정을 안해도 되긴 함.
    regdate=models.DateTimeField(default=datetime.now)
    views=models.IntegerField(default=0)
    contents=models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'board'
        ordering = ['-regdate']


    def __str__(self):
        return self.title
