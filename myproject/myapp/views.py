from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Post, Image
from .forms import PostForm, ImageForm

from django.core.exceptions import ObjectDoesNotExist

def index(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	list = []
	for post in posts:
		image = Image.objects.filter(post_id=post.pk)
		url = ''
		if image.count() != 0:
			url = image[0].image.url
		item = {'post': post, 'image': url}
		list.append(item)
	return render(request, 'index.html', {'list': list})

@login_required
def upload(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		form_image = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			url = ''
			if form_image.is_valid():
				image = form_image.save(commit=False)
				image.post_id = post
				url = image.image.url
				image.save()
			# post.thumbnail = url
			# post.save()
			return redirect('myapp.views.index')
	return render(request, 'upload.html')

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	images = Image.objects.filter(post_id=post_id)
	return render(request, 'detail.html', {'post': post, 'images': images})

def delete(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.delete()
	return redirect('myapp.views.index')
