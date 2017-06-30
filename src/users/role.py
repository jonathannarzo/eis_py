from django.contrib.auth.decorators import user_passes_test

def role_required(*role_id):
    def in_groups(user):
        if user.is_authenticated():
            if hasattr(user, 'profile') and bool(user.profile.role in role_id):
                return True
            elif user.is_superuser:
                return True
            return False
    return user_passes_test(in_groups)
