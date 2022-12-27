from django.views.generic import UpdateView, CreateView, ListView
from main.models import Opportunity
from django.urls import reverse_lazy
from django.forms import DateInput, DateTimeInput, NumberInput


# ===================================================================
# Common Utilities
# ===================================================================
def get_form(class_instance, class_defination, form_class=None):
    if form_class is None:
        form_class = class_instance.get_form_class()

    form = super(class_defination, class_instance).get_form(form_class)
    form.fields['first_name'].widget.attrs = {}
    form.fields['last_name'].widget.attrs = {}
    form.fields['address1'].widget.attrs = {}
    form.fields['address2'].widget.attrs = {}
    form.fields['city'].widget.attrs = {}
    form.fields["province"].widget.attrs = {}
    form.fields['postal_code'].widget = NumberInput(
        attrs={"type": "number", "pattern": "[0-9]{6}"}
        )
    form.fields['phone_number1'].widget = NumberInput(attrs={
        "type": "tel",
        "pattern": "[0-9]{10}",
    })
    form.fields['phone_number2'].widget = NumberInput(attrs={
        "type": "tel",
        "pattern": "[0-9]{10}",
    })
    form.fields['sin'].widget = NumberInput(attrs={
        "placeholder": "Please Enter Sin (9 DIGITS)",
        "type": "tel",
        "pattern": "[0-9]{9}",
    })
    form.fields['email'].widget.attrs = {"type": "email"}
    form.fields['agent'].widget.attrs = {}
    form.fields['dob'].widget = DateInput(
        attrs={"type": "date"}
        )
    form.fields['collection_amount'].widget.attrs = {}
    form.fields['last_agent'].widget.attrs = {}
    form.fields['collection_date'].widget.attrs = {}
    form.fields['last_crawl'].widget = DateTimeInput(
        attrs={"type": "datetime-local"}
        )
    form.fields['last_result'].widget = DateInput(
        attrs={"type": "date"}
        )
    form.fields["prioritize_local"].widget.attrs = {}
    form.fields["prioritize_global"].widget.attrs = {}
    form.fields["file_upload"].widget.attrs = { "accept": ".doc, .docx, .pdf"}

    return form

# ===================================================================
# View
# ===================================================================
class OpportunityCreate(CreateView):
    model = Opportunity
    fields = "__all__"
    slug_field = "id"

    def get_context_data(self, *args, **kwargs):
        context = super(OpportunityCreate, self).get_context_data(
            *args, **kwargs)
        context['create'] = "create"
        return context

    def get_form(self, form_class=None):
        return get_form(self, OpportunityCreate, form_class=form_class)


class OpportunitySaveAndEditView(OpportunityCreate):

    """Save instance and redirect page to update that instance"""


class OpportunitySaveCreateNew(OpportunityCreate):

    """Create and redirect back to create form to create next"""

    success_url = reverse_lazy("main:opportunity_create")


class OpportunityCreateView(OpportunityCreate):

    """redirect to listview after creating."""

    success_url = reverse_lazy("opportunity_list")


class OpportunityUpdate(UpdateView):
    """Base update model for Opportunity"""
    model = Opportunity
    fields = "__all__"
    slug_field = "id"

    def get_context_data(self, *args, **kwargs):
        context = super(OpportunityUpdate, self).get_context_data(
            *args, **kwargs)
        context['update'] = "update"
        context["id"] = self.kwargs.get("pk")
        return context

    def get_form(self, form_class=None):
        return get_form(self, OpportunityUpdate, form_class=form_class)


class OpportunityUpdateListView(OpportunityUpdate):

    """Updating individual opportunities."""

    success_url = reverse_lazy("opportunity_list")


class OpportunityUpdateEdit(OpportunityUpdate):

    """Update and redirect to edit the form."""
    pass


class OpportunityUpdateCreateView(OpportunityUpdate):
    """View to save updated data and redirect user to add new data"""

    success_url = reverse_lazy("main:opportunity_create")


class OpportunityListView(ListView):

    """Return all the list of added items."""

    model = Opportunity
