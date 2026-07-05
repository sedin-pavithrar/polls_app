from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'polls'


#Why not just "polls"?
#PollsConfig contains metadata about your application and is the recommended way to register apps. It also allows future configuration such as startup code.