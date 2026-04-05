from django import forms

from .models import Property, SiteEnquiry


class SiteEnquiryForm(forms.ModelForm):
    property_slug = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = SiteEnquiry
        fields = ("enquiry_type", "name", "phone", "message")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["message"].required = False
        self.fields["property_slug"].required = False

    def clean_phone(self):
        raw = (self.cleaned_data.get("phone") or "").strip()
        digits = "".join(c for c in raw if c.isdigit())
        if len(digits) != 10:
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return digits

    def clean(self):
        data = super().clean()
        etype = data.get("enquiry_type")
        slug = (data.get("property_slug") or "").strip()
        self._resolved_property = None

        if etype == SiteEnquiry.EnquiryType.CALLBACK:
            if not slug:
                raise forms.ValidationError(
                    {"property_slug": "Property reference is missing for this request."}
                )
            prop = (
                Property.objects.filter(slug=slug, is_published=True)
                .only("pk")
                .first()
            )
            if not prop:
                raise forms.ValidationError(
                    {"property_slug": "This property is not available for enquiries."}
                )
            self._resolved_property = prop
        return data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.property = getattr(self, "_resolved_property", None)
        if commit:
            instance.save()
        return instance
