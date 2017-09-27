from django.shortcuts import render, redirect
from django.views.generic import ListView, RedirectView, CreateView
from django.views import View
from .models import Post, MyComment
from django.core.urlresolvers import reverse_lazy, reverse
from collections import OrderedDict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Home(RedirectView):
	pattern_name = 'forum-posts'


class PostList(ListView):
	model=Post
	paginate_by = 10
	ordering = ['-created']


class PostView(View):
	model=MyComment
	template_name = 'forum/post_view.html'

	# returns an OrderedDict of { comment_id: [child_ids,]}
	def create_parent_dict(p_pk):
		d = OrderedDict()
		r = MyComment.objects.filter(post_id=p_pk)
		for elem in r:
			d.setdefault(elem.comment_id, [])
			d[elem.comment_id].append(elem)
		return d

	# returns a list of elements in order
	# d = OrderedDict returned by create_parent_dict()
	# c_pk = MyComment id of the parent elem
	# lst = the list where we will append everything
	# level = the depth level we are in
	# To get all the comments of one Post, this should be called with :
	# printable_dict(self, create_parent_dict(self))
	def printable_dict(d, c_pk=0, lst=[], level=0):
		if c_pk in d:
			for elem in d[c_pk]:
				lst.append([elem, level])
				PostView.printable_dict(d, elem.pk, lst, level + 1)

	def get(self, request, *args, **kwargs):
		if 'pk' in kwargs:
			d = PostView.create_parent_dict(kwargs['pk'])
			comments = []
			PostView.printable_dict(d=d, c_pk=0, lst=comments)
			post = Post.objects.get(pk=kwargs['pk'])
			context = {}
			context['comments'] = comments
			context['pk'] = kwargs['pk']
			context['post'] = post
			kwargs = None
			return render(request, self.template_name, context)
		else:
			return render(request, self.template_name, kwargs)


class PostForm(CreateView):
	model = Post
	fields = ['title', 'content']
	success_url = reverse_lazy('forum-posts')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(PostForm, self).form_valid(form)


class Comment(CreateView):
	model = MyComment
	fields = ['content', 'comment_id']

	def get_success_url(self, **kwargs):
		if  kwargs != None:
			return reverse_lazy('forum-detail', kwargs={ 'pk': self.kwargs['p_pk'] })
		else:
			return reverse_lazy('forum-posts')

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.post_id = self.kwargs['p_pk']
		form.instance.comment_id = form.cleaned_data['comment_id']
		super(Comment, self).form_valid(form)
		return redirect(self.get_success_url())

	def form_invalid(self, form):
		return redirect(self.get_success_url())









