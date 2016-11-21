from django.shortcuts import render, redirect
from models import Poke
from django.db.models import Sum
from ..login.models import User
from django.views.generic import View 
from django.core.urlresolvers import reverse

# Create your views here.
class Pokes(View):
	def get(self, request):
		#get all pokes

		if not 'user_id' in request.session:
			return redirect(reverse('login:index'))

		context = {
			'pokes': Poke.objects.all(),
			'loggeduser': User.objects.get(id=request.session['user_id']),
			'users': User.objects.all().annotate(total_pokes=Sum('pokesreceived__count')),
		}
		return render(request, 'belt_2/index.html', context)

	def post(self, request):
		#create poke
		user = User.objects.get(id=request.session['user_id'])
		print user
		userpoked = User.objects.get(id=request.POST['id'])
		print userpoked

		#if poke does not exist, create it
		poke = Poke.objects.filter(userpoking=user, userpoked=userpoked)
		print poke
		print len(poke)
		if len(poke) == 0:
			Poke.objects.create(userpoking=user, userpoked=userpoked)
		else:
			count = poke[0].count + 1
			poke.update(count=count)

		return redirect(reverse('pokes:pokes'))