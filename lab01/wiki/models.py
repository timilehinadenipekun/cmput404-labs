from django.db import models

# Create your models here.
class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()  # Markdown content
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.id} - {self.title}"

class Like(models.Model):
    page= models.ForeignKey(Page, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
