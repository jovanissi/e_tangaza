from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.homePage),

	url(r'^home', views.homePage),

	url(r'^(?P<ann_id>\d+)$', views.announcementDetails),

	url(r'^admin_(?P<ann_id>\d+)$', views.adminAnnouncementDetails),

	url(r'^lost-items', views.lostItemsPage),

	url(r'^found-items', views.foundItemsPage),

	url(r'^on-sale-items', views.onSalePage),

	url(r'^events', views.eventsPage),

	url(r'^jobs', views.jobsPage),

	url(r'^advertisements', views.advertisementsPage),

	url(r'^other-announcements', views.otherAnnouncementsPage),

	url(r'^postAnnouncementPage', views.postAnnouncementPage),

	url(r'^post-new-announcement', views.postNewAnnouncements),

	url(r'^admin-dashboard', views.pendingAnnouncements),

	url(r'^approve', views.approveAnnouncement),

	url(r'^reject', views.rejectAnnouncement),

	url(r'^login', views.login_page),

	url(r'^adminLogin', views.admin_login),

	url(r'^logout', views.logout),

	url(r'^search', views.searchAnnouncement),

	url(r'^invalid_login', views.invalidLogin),
]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)