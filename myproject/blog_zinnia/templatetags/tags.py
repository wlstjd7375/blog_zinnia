from django import template
register = template.Library()

@register.simple_tag
def get_popover_content(author):
    content = "name : " + author.name.__str__() + "<br>" + "email : " + author.email.__str__() + "<br>" + "url : " + author.url.__str__() + "<br>" + "intro : " + author.intro.__str__() + "<br>"
    return content

