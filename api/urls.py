from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('five-names', views.five_names, name='five_names'),
    # path('macro-nutrients/', views.macro_nutrients),
    path('test', views.test_pivot),
    path('macro-nutrients/', views.food_list),
    path('macro-nutrients/<str:pk>', views.food_detail),
    path('food-groups', views.food_groups),
]