from django.urls import include, path
from rest_framework import routers
from .views import GuestViewSet, EventViewSet, indexGuest, indexEvent, eventPage

router = routers.DefaultRouter()
router.register(r'guests', GuestViewSet)
router.register(r'events', EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('guests', GuestViewSet),
    path('events', EventViewSet),
    path('guestPost', indexGuest),
    path('eventPost', indexEvent),
    path('eventPage', eventPage),
    path('gvs', GuestViewSet.as_view()),
    path('evs', EventViewSet.as_view()),
    
]