from django.urls import include, path
urlpatterns = [
    path("wiki/", include("wiki.urls")),
    path("admin/", admin.site.urls),
]
