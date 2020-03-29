from django.db import models
from django.contrib.auth.models import User


class BlogUser(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	# displaypic = models.ImageField(upload_to='dps')

	def __str__(self):
		return self.user.username



class Post(models.Model):
	political = "Pol"
	scientific = "Sci"
	humour = "Hum"
	education = "Edu"
	employment = "Emp"
	general = "Gen"
	title = models.CharField(max_length = 50)
	content = models.TextField()
	Publisher = models.ForeignKey(BlogUser, on_delete = models.CASCADE)
	genre = models.CharField(max_length = 20, choices = ((political, "Political"), (scientific, "Scientific"), 	(humour, "Humour"), (education, "Education"), (employment, "Employmet"), (general, 	"General")))
	def __str__(self):
		return self.title

