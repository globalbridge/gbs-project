from django import template
import math
from datetime import datetime, timedelta
register = template.Library()

@register.filter(name='addcss')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})

def floor(value):
    return math.floor(value)

register.filter('floor', floor)

@register.filter
def age(value):
    now = datetime.now()
    try:
        difference = value - now.date()
        print difference.days
        return difference.days
    except Exception as e:
        print e
        return 0