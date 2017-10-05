from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.views import View
from django.views.generic import UpdateView
from django.core.exceptions import PermissionDenied
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from .models import UserProfile
from django.db import transaction
from django.core.urlresolvers import reverse_lazy, reverse

class UserProfileDetail(View):
	model = UserProfile
	template_name = 'userprofile/profile_detail.html'

	def get(self, request, *args, **kwargs):
		profile_user = User.objects.get(pk=self.kwargs['pk'])
		if request.user.is_authenticated() and (request.user == profile_user or self.request.user.groups.filter(name='super_user').exists() or self.request.user.is_superuser):
			return render(request, self.template_name, { 'object': UserProfile.objects.get(user=profile_user), 'pk': kwargs['pk']})
		return redirect(reverse_lazy('home'))

def add_privileges(request, pk):
	profile_user = User.objects.get(pk=pk)
	if not profile_user.groups.filter(name='super_user').exists():
		group = Group.objects.get(name='super_user')
		profile_user.groups.add(group)
		profile_user.save()
	return redirect('userprofile-edit', pk)

def remove_privileges(request, pk):
	profile_user = User.objects.get(pk=pk)
	if profile_user.groups.filter(name='super_user').exists():
		group = Group.objects.get(name='super_user')
		profile_user.groups.remove(group)
		profile_user.save()
	return redirect('userprofile-edit', pk)

class UserProfileEdit(View):
	template_name = 'userprofile/userprofile_edit.html'

	def get(self, request, *args, **kwargs):
		print(">>>> GET VIEW")
		context = {}
		context['is_admin'] = self.request.user.groups.filter(name='super_user').exists()
		profile_user = User.objects.get(pk=self.kwargs['pk'])
		context['profile_is_admin'] = profile_user.groups.filter(name='super_user').exists()
		if self.request.user.is_authenticated() and (self.request.user.pk == int(self.kwargs['pk']) or self.request.user.groups.filter(name='super_user').exists() or self.request.user.is_superuser):
			context['p_user'] = profile_user
			context['userprofile'] = UserProfile.objects.get(user=self.kwargs['pk'])
			context['pk'] = self.kwargs['pk']
		else:
			context['userprofile'] = None
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		print(">>>>> POST VIEW")
		if self.request.user.is_authenticated() and (self.request.user.pk == int(self.kwargs['pk']) or self.request.user.groups.filter(name='super_user').exists() or self.request.user.is_superuser):
			print(">>> USER OK")
			user = User.objects.get(pk=self.kwargs['pk'])
			myuser = UserProfile.objects.get(user=self.kwargs['pk'])
			if 'firstname' in request.POST:
				user.first_name = request.POST['firstname'][:30]
				user.save()
			if 'lastname' in request.POST:
				user.last_name = request.POST['lastname'][:30]
				user.save()
			if 'email' in request.POST:
				user.email = request.POST['email'][:150]
				user.save()
			if 'description' in request.POST:
				print(request.POST['description'])
				myuser.description = request.POST['description']
				myuser.save()
			if 'picture' in request.FILES:
				print(request.FILES['picture'])
				myuser.picture = request.FILES['picture']
				myuser.save()
			return redirect('userprofile-edit', self.kwargs['pk'])
		return redirect('userprofile-home', self.kwargs['pk'])

