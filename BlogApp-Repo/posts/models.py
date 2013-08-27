from django.db import models

class blogPost(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	postdate = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title