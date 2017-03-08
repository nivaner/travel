# -*- coding: utf-8 -*-
from django.conf.urls import url
# import views
# import views.guide as guide_view
import views.community as communitys

# guide =views.guide
community_view = communitys.Community()
urlpatterns = [
    url(r'^$', community_view.get_community),
    url(r'^view/(?P<category>\w+)/(?P<action>\w+)/$', community_view.get_probem_list),
]

urls = urlpatterns
