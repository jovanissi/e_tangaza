from django.db import models
from datetime import datetime

# Create your models here.

class Announcement(models.Model):
	Name = models.CharField(max_length=50, help_text="The name of the announcer")
	Phone = models.CharField(max_length=50, help_text="Phone number of the announcer")
	Email = models.CharField(max_length=50, help_text="Email of the announcer", default='null')
	lost = 'lost'
	found = 'found'
	on_sale = 'on_sale'
	event = 'event'
	job = 'job'
	advertisement = 'advertisement'
	announcement = 'announcement'
	categories = {
		(lost, 'lost'),
		(found, 'found'),
		(on_sale, 'on_sale'),
		(event, 'event'),
		(job, 'job'),
		(advertisement, 'advertisement'),
		(announcement, 'announcement'),
	}
	Category = models.CharField(max_length=20, choices=categories, default='announcement', help_text="The category of the announcement")
	Title = models.TextField(help_text="The title of the announcement")
	Announcement = models.TextField(help_text="The announcement (description of the announcement)")
	Date = models.DateTimeField(default=datetime.now)
	pending = 'pending'
	approved = 'approved'
	rejected = 'rejected'
	types = {
		(pending, 'pending'),
		(approved, 'approved'),
		(rejected, 'rejected'),
	}
	Type = models.CharField(max_length=20, choices=types, default='pending', help_text="The type of the announcement. This is whether it is rejected, approved, or pending")
	Icon = models.FileField(upload_to='announcement-icon', default='null')

	def __str__(self):
		return str(self.Name) + " " + str(self.Date)
