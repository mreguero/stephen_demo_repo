@given(u'some precondition')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given some precondition')

@when(u'some action by the actor')
def step_impl(context):
    raise NotImplementedError(u'STEP: When some action by the actor')

@then(u'some testable outcome is achieved')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then some testable outcome is achieved')

