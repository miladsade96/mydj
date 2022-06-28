from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag(name="n_published_posts")
def get_number_of_published_posts():
    return Post.objects.filter(status=1).count()
