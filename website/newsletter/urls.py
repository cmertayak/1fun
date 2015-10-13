from django.conf.urls import url

from .views import NewsletterView

urls = [
    url(r'^$', NewsletterView.as_view(), name='newsletter')
]

#patterns('', url(r'^$', NewsletterView.as_view() , name='newsletter'))