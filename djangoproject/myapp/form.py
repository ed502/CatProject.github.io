from django import forms

# 모델에서 정의한 PolicyList 
from .models import free_list
from .models import detect_list

class free_list(forms.ModelForm):
    class Meta:
        model = free_list

        # 모든 항목 입력받으려묜...
        # fields = '__all__'
        
        fields = ['title','body']

class detect_list(forms.ModelForm):
    class Meta:
        
        model = detect_list

        # 모든 항목 입력받으려묜...
        # fields = '__all__'
        
        fields = ['title','body']