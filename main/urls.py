from django.urls import path
from main.views import (
                        OpportunityCreateView, OpportunityUpdateListView,
                        OpportunitySaveCreateNew, OpportunitySaveAndEditView,
                        OpportunityUpdateEdit, OpportunityUpdateCreateView
                    )


app_name = "main"

urlpatterns = [
    path(
        'create',
        OpportunityCreateView.as_view(),
        name="opportunity_create"
    ),
    path(
        '<int:pk>',
        OpportunityUpdateListView.as_view(),
        name="opportunity_update"
    ),
    path(
        'create/new',
        OpportunitySaveCreateNew.as_view(),
        name="save_and_create_new"
    ),
    path(
        'create/edit',
        OpportunitySaveAndEditView.as_view(),
        name="save_and_update"
    ),
    path(
        'update/new/<int:pk>',
        OpportunityUpdateCreateView.as_view(),
        name="opportunity_update_create_new"
    ),
    path(
        'update/edit/<int:pk>',
        OpportunityUpdateEdit.as_view(),
        name="opportunity_update_edit"
    )
]
