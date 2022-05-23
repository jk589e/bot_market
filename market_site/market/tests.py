from django.test import TestCase

# Create your tests here.
from django.utils.safestring import mark_safe
a = mark_safe('<img src="{0}" width="150" height="150" />'.format("images/default_pic.png"))
print(a)