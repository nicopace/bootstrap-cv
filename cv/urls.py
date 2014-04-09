from django.conf.urls import url, patterns

urlpatterns = patterns('cv.views',
        url(r'(?P<nombre_completo>\D+)/$', 'view_cv'),
)
