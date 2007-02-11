# (c) 2006 Nuxeo SARL <http://nuxeo.com>
# Author: Mehdi Baccouche <mailto:mbaccouche@nuxeo.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
#
# $Id$

__author__ = "Mehdi Baccouche <mailto:mbaccouche@nuxeo.com>"

"""CPSTaskManager

CPSTaskManager is a task tracker intended to be used with CPS version 3.

You can access the software requierements specifications within
the docs sub-directory of the product.
"""

##############################################
# PATCHING THE OFS.
##############################################

# I have to give the member the "Delete objects"
# permissions for them being able to delete their own tasks.
# But I don't want them to that for someone else's task.

from cgi import escape

from OFS.ObjectManager import ObjectManager
from AccessControl import ClassSecurityInfo
from Globals import MessageDialog

from Products.CMFCore.DirectoryView import registerDirectory

from Products.GenericSetup import profile_registry
from Products.GenericSetup import EXTENSION

from Products.CPSCore.interfaces import ICPSSite

security = ClassSecurityInfo()

security.declareProtected("View", "manage_delObjects")

import sys

from Products.CMFCore.utils import ToolInit, ContentInit
from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFCore.CMFCorePermissions import AddPortalContent

#import PatchSQLDirectory

registerDirectory('skins', globals())

def initialize(context):
    """
    Registering the content of the module
    """
    
    profile_registry.registerProfile(
        'default',
        'CPS Task Manager',
        "Simple Task Manager for CPS.",
        'profiles/default',
        'CPSTaskManager',
        EXTENSION,
        for_=ICPSSite)
