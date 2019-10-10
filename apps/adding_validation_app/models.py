from django.db import models

# Create your models here.
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors

    def blog_creater(self, postData):
        blog_res = {
            'validate': True,
            'blog': None
        }

        b = Blog.objects.create(name=postData['name'], desc=postData['desc'])
        b.save()
        blog_res['blog'] = b
        return blog_res


class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()