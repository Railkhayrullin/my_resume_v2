import os
from .general import BASE_DIR


STATIC_URL = '/billing/static/'
STATIC_ROOT = os.path.join(BASE_DIR.parent, 'static')
# STATICFILES_DIRS = (
#     os.path.normpath(os.path.join(BASE_DIR, '../client/src/build')),
# )


MEDIA_URL = '/billing/media/'
MEDIA_ROOT = BASE_DIR.parent
