from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	date = models.DateField()
	image = models.ImageField(upload_to="images")
	body = models.TextField()

	def __str__(self):
		return self.title + " | " + str(self.date)


class Resume(models.Model):
	date = models.DateField()
	pdf = models.FileField(upload_to="images")

	def __str__(self):
		return self.pdf.name.split("/")[1] + " | " + str(self.date)


class RightSideBarContent(models.Model):
	date = models.DateField()
	body = models.TextField()

	def __str__(self):
		return "Content | " + str(self.date)


class Video(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateField()
	video_id = models.CharField(max_length=255)

	def __str__(self):
		return self.title + " | " + str(self.date)
