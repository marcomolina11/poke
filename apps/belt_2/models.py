from __future__ import unicode_literals
from django.db import models
from ..login.models import User

# Create your models here.
# class PokeManager(models.Manager):
# 	def createPoke(self, request, id):
# 		userpoking = User.objects.get(id=request.session['user_id'])
# 		userpoked = User.objects.get(id=id)

# 		poke = self.create(userpoking=userpoking, userpoked=userpoked)
# 		return(True, note)

# 	def updatePokeCount(self, request, id):


class Poke(models.Model):
	userpoking = models.ForeignKey(User, related_name="pokesmade")
	userpoked = models.ForeignKey(User, related_name="pokesreceived")
	count = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# PokeManager = PokeManager()
	# objects = models.Manager()

	class Meta:
		ordering = ['-count']