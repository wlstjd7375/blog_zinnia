from django import forms
from .models import Post
from .models import Image

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ('image',)

