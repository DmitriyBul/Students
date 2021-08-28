from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag
def edit(user):
    search_user = User.objects.get(username=user)
    link = '<a href="/admin/auth/user/' + str(search_user.id) + '/' + '/change/">' + '</a>'
    return link
