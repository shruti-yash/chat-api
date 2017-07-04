from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('', filename)

class Message(models.Model):
	send_by = models.ForeignKey(User, related_name='send_by', on_delete=models.CASCADE)
	send_to = models.ForeignKey(User, related_name='send_to', on_delete=models.CASCADE)
	text = models.CharField(max_length=1024, blank=True, null=True, default='')
	ufile = models.FileField(upload_to=get_file_path, blank=True, null=True, default='')
	created_at = models.DateTimeField(auto_now_add=True)