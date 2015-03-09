from __future__ import unicode_literals

import os.path

from django import forms
from django.contrib.admin.helpers import ActionForm
from django.utils.translation import ugettext_lazy as _
import logging
logger = logging.getLogger(__name__)

class ImportForm(forms.Form):
    import_file = forms.FileField(
            label=_('File to import')
            )
    input_format = forms.ChoiceField(
            label=_('Format'),
            choices=(),
            )

    def __init__(self, import_formats, *args, **kwargs):
        super(ImportForm, self).__init__(*args, **kwargs)
        choices = []
        for i, f in enumerate(import_formats):
            choices.append((str(i), f().get_title(),))
        if len(import_formats) > 1:
            choices.insert(0, ('', '---'))

        self.fields['input_format'].choices = choices


class ConfirmImportForm(forms.Form):
    import_file_name = forms.CharField(widget=forms.HiddenInput())
    input_format = forms.CharField(widget=forms.HiddenInput())

    def clean_import_file_name(self):
        data = self.cleaned_data['import_file_name']
        data = os.path.basename(data)
        return data


class ExportForm(forms.Form):
    file_format = forms.ChoiceField(
            label=_('Format'),
            choices=(),
            )
    export_fields = forms.MultipleChoiceField(
            label=_('Fields to Export'),
            choices=(),
            )
    def __init__(self, formats, export_fields, *args, **kwargs):
        super(ExportForm, self).__init__(*args, **kwargs)
        choices = []
        fields = []
        for i, f in enumerate(formats):            
            choices.append((str(i), f().get_title(),))
        if len(formats) > 1:
            choices.insert(0, ('', '---'))
        
        for i, f in enumerate(export_fields):
            fields.append((str(i),f))
        self.fields['file_format'].choices = choices
        self.fields['export_fields'].choices = fields
       # logger.info("formats = %s", choices)
       # logger.info("export_fields = %s", fields)

def export_action_form_factory(formats):
    """
    Returns an ActionForm subclass containing a ChoiceField populated with
    the given formats.
    """
    class _ExportActionForm(ActionForm):
        """
        Action form with export format ChoiceField.
        """
        file_format = forms.ChoiceField(
            label=_('Format'), choices=formats, required=False)
    _ExportActionForm.__name__ = str('ExportActionForm')

    return _ExportActionForm
