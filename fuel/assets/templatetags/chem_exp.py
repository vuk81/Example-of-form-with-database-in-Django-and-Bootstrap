from django import template
import datetime
register = template.Library()

@register.filter(is_safe=True)
def chemical_expired(item):
		#Funcion calculates difference between today date and date of expiry
		#If difference is less then 30 days (2 592 000 seconds) it displays row in red color as a warning
		delta = item.data_expire - datetime.date.today()
		if delta.total_seconds() < 2592000:
			expire = True
		else:
			expire = False
		return expire