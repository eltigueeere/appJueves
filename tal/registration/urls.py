from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate, CondicionesPageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('condiciones/', CondicionesPageView.as_view(), name="condiciones"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
]