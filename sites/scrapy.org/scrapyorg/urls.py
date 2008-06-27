from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings


urlpatterns = patterns('',
    (r"^$", direct_to_template, { "template": "home.html" }),
    (r"^article/", include("scrapyorg.article.urls")),
    (r"^download/", include("scrapyorg.download.urls")),
    (r"^link/", include("scrapyorg.link.urls")),
    (r"^weblog/", include("scrapyorg.blog.urls")),

    (r"^admin/", include("django.contrib.admin.urls")),
)


if settings.DEBUG: # devel
    urlpatterns += patterns('',         
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
