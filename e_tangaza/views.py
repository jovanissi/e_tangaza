from django.shortcuts import render, redirect
from .models import *
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files import File
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
from django.core.mail import EmailMessage

# Create your views here.


def homePage(request):
	data = {}
	data['all_announcements'] = Announcement.objects.filter(Type='approved').order_by('-Date')

	return render(request, 'index.html', data)


def announcementDetails(request, ann_id):
	data = {}
	data['announcement'] = Announcement.objects.get(pk=ann_id)

	return render(request, 'announcement-details.html', data)


def adminAnnouncementDetails(request, ann_id):
	data = {}
	data['announcement'] = Announcement.objects.get(pk=ann_id)

	return render(request, 'admin-announcement-details.html', data)


def lostItemsPage(request):
	data = {}
	data['all_announcements'] = Announcement.objects.filter(Category='lost', Type='approved').order_by('-Date')

	return render(request, 'index.html', data)


def foundItemsPage(request):
	data = {}
	data['all_announcements'] = Announcement.objects.filter(Category='found', Type='approved').order_by('-Date')

	return render(request, 'index.html', data)


def onSalePage(request):
	data = {}
	data['all_announcements'] = Announcement.objects.filter(Category='on_sale', Type='approved').order_by('-Date')

	return render(request, 'index.html', data)


def eventsPage(request):
	data = {}
	data['all_announcements'] = Announcement.objects.filter(Category='event', Type='approved').order_by('-Date')

	return render(request, 'index.html', data)


def jobsPage(request):
	data = {}
	data['all_announcements'] = Announcement.objects.filter(Category='job', Type='approved').order_by('-Date')

	return render(request, 'index.html', data)


def advertisementsPage(request):
	data = {}
	data['all_announcements'] = Announcement.objects.filter(Category='advertisement', Type='approved').order_by('-Date')

	return render(request, 'index.html', data)


def otherAnnouncementsPage(request):
	data = {}
	data['all_announcements'] = Announcement.objects.filter(Category='announcement', Type='approved').order_by('-Date')

	return render(request, 'index.html', data)


def postAnnouncementPage(request):
	return render(request, 'post-announcement.html')


def postNewAnnouncements(request):
	name = request.POST['name']
	phone = request.POST['phone']
	email = request.POST['email']
	category = request.POST['category']
	title = request.POST['title']
	announcement = request.POST['announcement']
	icon = request.FILES['icon']
	Announcement.objects.create(
		Name = name,
		Phone = phone,
		Email = email,
		Category = category,
		Title = title,
		Announcement = announcement,
		Icon = icon
		)
	latest_ann = Announcement.objects.filter(Phone=phone).last()
	latest_ann_id = latest_ann.id
	message_to_send = "You have received new announcement from" + " " + str(name) + " " + "with the email" + " " + str(email) + "\n\nAnnouncement id is:" + " " + str(latest_ann_id)
	eMail = EmailMessage('New announcement sent', message_to_send, to=['nissijova@gmail.com'])
	eMail.send()
	message_to_send_to_user = "Hello" + " " + str(name) + "," + "\n\nThe announcement id is: " + str(latest_ann_id) + ".\nYou will use this id as the reference number while paying for your announcement to be approved. \nThank you. \n\nNB: The announcement is only seen by others on the platform only if you have completed the payment."
	eMail_2 = EmailMessage('eTangaza Ltd', message_to_send_to_user, to=[email])
	eMail_2.send() 
	return render(request, 'post-announcement.html', {"success": "success"})


def login_page(request):
	return render(request, 'admin-login.html')

# def admin_login(request):
# 	username = request.POST.get('username', '')
# 	password = request.POST.get('password', '')
# 	user = auth.authenticate(username=username, password=password)
# 	if user is not None:
# 		auth.login(request, user)
# 		return HttpResponseRedirect('pendin-ann')
# 	else:
# 		return HttpResponseRedirect('login')

def admin_login(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('admin-dashboard')
	else:
		return HttpResponseRedirect('invalid_login')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('login')


@login_required(login_url="login")
def pendingAnnouncements(request):
	data = {}
	data['pending_announcements'] = Announcement.objects.filter(Type='pending').order_by('-Date')

	return render(request, 'admin-dashboard.html', data)

@login_required(login_url="login")
def approveAnnouncement(request):
	x = request.POST['id']
	Announcement.objects.filter(id=x).update(Type='approved')
	ann = Announcement.objects.get(id=x)
	eMail = ann.Email

	message_to_send = "Hello" + " " + str(ann.Name) + "," + "\n\nYour announcement has been approved. Now it can be seen who visits the platform. \nPlease contact our team for more information. \nThank you."
	email = EmailMessage('Your announcement has been approved', message_to_send, to=[eMail])
	email.send()
	return HttpResponseRedirect('pending-ann')

@login_required(login_url="login")
def rejectAnnouncement(request):
	x = request.POST['id']
	Announcement.objects.filter(id=x).update(Type='rejected')
	ann = Announcement.objects.get(id=x)
	eMail = ann.Email
	
	message_to_send = "Hello" + " " + str(ann.Name) + "," + "\n\nYour announcement has been rejected for some unmet reasons. \nPlease contact our team for more information. \nThank you."
	email = EmailMessage('Your announcement has been rejected', message_to_send, to=[eMail])
	email.send()
	return HttpResponseRedirect('pending-ann')


def searchAnnouncement(request):
	x = request.GET.get('words')
	words = str(x)
	data = {}
	data['all_announcements'] = Announcement.objects.filter(Announcement__contains=x)|Announcement.objects.filter(Title__contains=x)|Announcement.objects.filter(Name__contains=x).order_by('-Date')

	return render(request, 'index.html', data)




def invalidLogin(request):
	return render(request, 'invalid-login.html')
