from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Page, Like
# Create your views here.

def editor(request):
	return render(request, "editor.html")
def index(request):
	pages = []

	page_objects = Page.objects.all()
	for page in page_objects:
		pages.append({
			"title": page.title,
			"url": reverse("view", kwargs={ "id": page.id })
        })
	return render(request, "index.html", { "pages": pages })
def view_page(request, id):
	page = get_object_or_404(Page, pk=id)
	like_count = page.like_set.count()
	return render(request, "page.html", { "title": page.title, "content": page.content, "id": id, "like_count": like_count })

def savePage(request):
	if request.method =="POST":
		title =request.POST.get("title")
		content=request.POST.get("content")
	Page.objects.create(
		title=title,
		content=content)
	return redirect("/wiki/")

def like_page(request, id):
	page = get_object_or_404(Page, pk=id)

	if request.method == "POST":
        	like = Like(page=page)
        	like.save()
	return redirect("/wiki/page/" + str(id) + "/")

def view_likes(request, id):
	page = get_object_or_404(Page, pk=id)
	like_objects = Like.objects.filter(page=page)
	likes = []
	for like in like_objects:
        	likes.append(str(like.created_at))
	return render(request, "likes.html", {
        	"id": id,
        	"title": page.title,
        	"likes": likes
    })
