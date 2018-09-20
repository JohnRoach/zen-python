from behave import given, then


@given(u'Zen is set up')
def zen_setup(context):
    assert context.client

@when('A request for the endpoint "{route}"')
def basic_route_get(context, route):
    context.page = context.client.get(route)
    assert context.page

@then('a 200 response with OK in the body is returned')
def successful_health_check(context):
    assert context.page.status_code == 200
    assert context.page.text == "OK"
