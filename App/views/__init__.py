# blue prints are imported 
# explicitly instead of using *

from .user import user_views
from .auth import auth_views
from .course import course_views
from .index import index_views





views = [auth_views, course_views, index_views, user_views] 
# blueprints must be added to this list