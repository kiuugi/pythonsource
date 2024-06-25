from django import forms
from .models import Photo


# ModelForm : 모델과 연결된 폼
#   Photo 모델의 필드를 모두 가지고 있는 상태
# DTO랑 비슷한듯
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
