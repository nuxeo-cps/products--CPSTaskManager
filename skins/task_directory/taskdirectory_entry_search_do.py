##parameters=dir, datastructure, **kw
# $Id$

from Products.CPSDirectory.BaseDirectory import SearchSizeLimitExceeded

datamodel = datastructure.getDataModel()

mapping = {}
for key, value in datamodel.items():
    if value:
        mapping[key] = value

result_fields = context.getDirectoryResultFields(dir.getId(),
                                                 dir.title_field)

return_fields = []
sort_by = None
sort_direction = None
process_fields = {}
for field in result_fields:
    return_fields.append(field['id'])
    sorted = field.get('sort')
    if sorted == 'asc':
        sort_by = field['id']
        sort_direction = 'asc'
    elif sorted == 'desc':
        sort_by = field['id']
        sort_direction = 'desc'
    if field.get('process'):
        process_fields[field['id']] = field['process']

# 'responsable' field is needed for filtering the results
if 'responsable' not in return_fields:
    return_fields.append('responsable')
# empty search will not return anything
if not mapping:
    return dir.taskdirectory_entry_search_results(results=[]), 'results'

try:
    results = dir.searchEntries(return_fields=return_fields, **mapping)
except SearchSizeLimitExceeded, e:
    rendered = dir.taskdirectory_entry_search_errors(exception=e)
    return rendered, 'results'

for field, process_meth in process_fields.items():
    meth = getattr(context, process_meth, None)
    if not meth:
        continue
    for item in results:
        value = item[1].get(field)
        item[1][field] = meth(field, value)

member = context.portal_membership.getAuthenticatedMember()
if member:
    member_id = member.getMemberId()
else:
    member_id = ''
new_results = []
for item in results:
    # filter the entries: createur OR responsable should be the current user
    createur = item[1].get('createur')
    responsable = item[1].get('responsable')
    if member_id in (createur, responsable):
        new_results += item,
results = new_results

if sort_by:
    items = [(str(item[1].get(sort_by, 'ZZZZ')).lower(), item) for item in results]
    items.sort()
    if sort_direction == 'desc':
        items.reverse()
    results = [item[1] for item in items]

rendered = dir.taskdirectory_entry_search_results(results=results)

return rendered, 'results'
