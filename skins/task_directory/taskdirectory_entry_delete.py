##parameters=dirname=None, id=None, ids=[], REQUEST=None
# $Id$
"""
This script can be both called with request parameters or with form parameters
"""

from zLOG import LOG, DEBUG
logKey = 'taskdirectory_entry_delete'

if REQUEST is not None:
    psm = 'psm_entry_deleted'
    if REQUEST.form.has_key('dirname'):
        dirname = REQUEST.form.get('dirname')
        #LOG(logKey, DEBUG, "dirname = %s" % dirname)

    if REQUEST.form.get('ids'):
        ids = REQUEST.form.get('ids')
        #LOG(logKey, DEBUG, "ids = %s" % str(ids))

dir = context.portal_directories[dirname]

if id:
    try:
        dir.deleteEntry(id)
    except ValueError, e:
        msg = str(e)
        if REQUEST is not None and \
               msg.find("Operation not allowed on non-leaf") > 0:
            psm = 'psm_entry_delete_not_allowed_on_non_leaf'
        else:
            raise

if ids:
    for id in ids:
        dir.deleteEntry(id)

if REQUEST is not None:
    portal_url = context.portal_url()
    REQUEST.RESPONSE.redirect('%s/taskdirectory_entry_search_form?dirname=%s'
                              '&portal_status_message=%s' %
                              (portal_url, dirname, psm))
