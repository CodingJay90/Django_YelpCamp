from django import template

register = template.Library()


@register.simple_tag
def underscoreTag(obj, attribute):
    # print(obj)
    # print(attribute)
    obj = dict(obj)
    return obj.get(attribute)
