@given(u'some')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given some')

@when(u'some')
def step_impl(context):
    raise NotImplementedError(u'STEP: When some')

@then(u'some')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then some')

