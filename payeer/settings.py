from django.conf import settings

PAYEER = getattr(settings, 'PAYEER', {})

PAYEER_ALLOWED_IPS = ('185.71.65.92', '185.71.65.189', '149.202.17.210')