from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from posts.forms import PostForm
from django.template import RequestContext

# Create your views here.

def post_create(request): # create new post/item
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("title")
		print form.cleaned_data.get("content")
		instance.save()
		messages.success(request, "successfully created")
		return HttpResponseRedirect(instance.get_absoulte_url())
	# else:
	# 	messages.error(request, "Problem creating the new post")	
	# if request.method == "POST":
	# 	title = request.POST.get("title")
	# 	content = request.POST.get("content")
	# 	Post.objects.create(title = title)
	context ={
		"form" : form,
	}
	return render(request, "post_form.html", context)
	# return HttpResponse("<h2>Create</h2>")

def post_detail(request, id = None): # on click on particluar item we see all the items
	#instance = Post.objects.get(id = 1) # if we do like this, if the id doesn't exist we will get error to overcome this we will use  #get_object_or_404
	instance = get_object_or_404(Post, id = id)
	context = {
		"title" : instance.title,
		"instance" : instance
	}
	return render(request, "post_detail.html", context)
	#return HttpResponse("zx<h2>Detail</h2>")

def post_list(request): # show all posts/items in the initial page
	queryset_list = Post.objects.all().order_by("-timestamp")
	paginator = Paginator(queryset_list, 10)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list" : queryset,
		"title" : "List",
		"page_request_var" :page_request_var,
	}

	# if  request.user.is_authenticated():
	# 	context = {
	# 		"title" : "My User List"
	# 	}
	# else:
	# 	context = {
	# 		"title" : "List"
	# 	}
	return render(request, "post_list.html", context)
	#return HttpResponse("<h2>List</h2>")

def post_update(request, id = None ): # edit the post/item
	instance = get_object_or_404(Post, id = id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Successfully</a> updated", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absoulte_url())	
	# else:
	# 	messages.error(request,"problem in updating the post")


	context = {
		"title" : instance.title,
		"instance" : instance,
		"form" : form,
	}
	return render(request, "post_form.html", context)

def post_delete(request, id=None): # delet the post/item
	instance = get_object_or_404(Post,id =id)
	instance.delete()
	messages.success(request, "successfully deleted")
	return redirect("posts:list")

def test(request):
	context = {
		"post": Post.objects.all(),
	}
	return render(request, "test.html",context)






