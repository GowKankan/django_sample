from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"] ## to add more columns in admin panel of 
			#default will be Post  but now we have added updated and timestamp and we have renamed Post to Title
	list_display_links = ["updated"] # we can have hyper link for Updated field
	list_filter = ["updated", "timestamp"] # now we have filter optio for both updated and timstamp field to right in admin page		
	search_fields = ["title", "content"] # this will add search field in admin panel at the top and we can search for the content
	list_editable = ["title"]
	class Meta:
		model = Post

# Register your models here.
admin.site.register(Post, PostModelAdmin)