from constants.django import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("user.urls")),
]
