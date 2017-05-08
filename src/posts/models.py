from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# from django.urls import reverse

# Create your models here.
class Post(models.Model):

	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def __str__(self):		
		return self.title

	def get_absoulte_url(self):
		return reverse("posts:detail" , kwargs={ "id" : self.id })
		#return "/posts/%s/" %(self.id)	# this is replaced with reverse above , as /posts/ -- we have give it in url.py name = 'detail'

	class Meta:
		ordering = ["-timestamp" ,"-updated"]	


