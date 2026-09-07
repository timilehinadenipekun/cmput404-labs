from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Page
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
	return render(request, "page.html", { "title": page.title, "content": page.content, "id": id })

def savePage(request):
	if request.method =="POST":
		title =request.POST.get("title")
		content=request.POST.get("content")
	Page.objects.create(
		title=title,
		content=content)
	return redirect("/wiki/")

