
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products<int:myid>/", views.productview, name="Productview"),
    path("checkout/", views.checkout, name="Checkout"),
        

    path("home/", views.home, name="Home"),
    path("signup/", views.signup, name="Signup"),
    path("login/",views.login, name="Login"),
    path("logout/", views.logout, name="Logout")
        
]
