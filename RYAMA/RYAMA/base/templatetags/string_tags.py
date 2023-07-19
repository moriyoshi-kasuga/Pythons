from django import template

register = template.Library()


@register.filter()
def newLine(value):
    return value.replace("<br>", r"\A")
