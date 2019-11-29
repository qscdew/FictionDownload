#!/use/bin/env python
# _*_ coding:utf-8 __

from django.contrib.sitemaps import Sitemap
import homepage.models
import homepage.forms


class BlogSitemap(Sitemap):
    changefreq = "daily"  # 每天发布
    priority = 1.0  # 优先级，最大1.0
    protocol = 'http'  # 站点是http还是https类型

    def items(self):
        # 获取所有被标记为已发布的文章，必须是一个列表
        return homepage.models.Bookinfo.objects.order_by('length')

    def lastmod(self, obj):
        # 创建时间
        return obj.last_modified_time

    def location(self, item):
        # URL
        return 'http://mikoto.site/books/' +str(item.id)