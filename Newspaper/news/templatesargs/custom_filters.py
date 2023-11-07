from django import template
import profanity as pf

register = template.Library() 


@register.filter(name='censor')
def censor(value):
    return pf.censor(value)

@register.filter(name ='is_profane')
def is_profane(value):
    return pf.is_profane(value)