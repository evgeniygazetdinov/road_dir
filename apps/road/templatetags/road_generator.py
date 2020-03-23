import datetime
from django import template
import random


register = template.Library()






@register.simple_tag
def generate_road(quan_lines):
    return quan_lines





