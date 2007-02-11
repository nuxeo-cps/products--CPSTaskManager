##parameters=directory_id, default_field=None
# $Id$
"""
Get the list of fields to be displayed in the directory search result list.
"""


fields = []

if directory_id == 'task':
    fields = [{'id': 'titre', 'title': '_portal_type_CPS_Task'},
              {'id': 'date_debut', 'title': '_label_start_date', 'sort': 'asc'},
              {'id': 'date_fin', 'title': '_label_stop_date'},
              {'id': 'createur', 'title': '_label_creator'},
              {'id': 'responsable', 'title': 'label_cps_task_member'},
              {'id': 'priorite', 'title': '_label_priority'},
              {'id': 'percentage', 'title': 'label_cps_task_percentage'},
              {'id': 'etat', 'title': '_label_state'},]

return fields
