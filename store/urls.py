from django.urls import path
from store import views

urlpatterns = [
    path("stores", views.store_list, name="Store List"),
    path("visit_store", views.create_visit, name="Create Visit"),
]
