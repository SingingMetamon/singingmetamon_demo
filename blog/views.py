from django.shortcuts import render
from django.utils import timezone
from .models import User_origin
from .models import User_modified
from .models import Singer_origin



def test(request):
    posts = Singer_origin.objects.filter(name='이건 테스트')
    return render(request, 'blog/test.html')