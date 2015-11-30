@given(u'given')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given given')

@when(u'when')
def step_impl(context):
    raise NotImplementedError(u'STEP: When when')

@then(u'then')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then then')

