import os
from .general import BASE_DIR


STATIC_URL = '/resume/static/'
STATIC_ROOT = os.path.join(BASE_DIR.parent, 'static')
# STATICFILES_DIRS = (
#     os.path.normpath(os.path.join(BASE_DIR, "static")),
# )

MEDIA_URL = '/resume/media/'
MEDIA_ROOT = BASE_DIR.parent
