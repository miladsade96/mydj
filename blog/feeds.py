from django.contrib.syndication.views import Feed
from blog.models import Post


class LatestPostsRSSFeed(Feed):
    title = "Latest posts on my blog"
    link = "/rss/feed/"
    description = "The latest posts on my blog"


    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100] + "..."
