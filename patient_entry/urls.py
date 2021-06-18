from django.urls import path,include
from patient_entry import views

app_name = 'processed_data'

urlpatterns = [
    path('search_by_address/',views.search_by_address,name='search_by_address'),
    path('search_by_name/',views.search_by_name,name='search_by_name'),
    path('see_collection_for_duration/',views.see_collection_for_duration,name='see_collection_for_duration'),
    path('collection_for_day',views.collection_for_day,name='collection_for_day'),
    path('options',views.Options.as_view(),name='options'),
    ]
