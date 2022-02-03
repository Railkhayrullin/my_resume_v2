import os
from .general import BASE_DIR


STATIC_URL = '/resume/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (
#     os.path.normpath(os.path.join(BASE_DIR.parent, 'static')),
# )

MEDIA_URL = '/resume/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
