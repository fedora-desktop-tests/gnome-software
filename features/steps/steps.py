# -*- coding: UTF-8 -*-
from behave import step

from dogtail.tree import root
from behave_common_steps.app import *
from behave_common_steps.appmenu import *
import tempfile
from dogtail.rawinput import typeText
import os.path
from dogtail.rawinput import drag


@step(u'Help section "{name}" is displayed')
def help_is_displayed(context, name):
    context.yelp = root.application('yelp')
    frame = context.yelp.child(roleName='frame')
    context.assertion.assertEquals(name, frame.name)
