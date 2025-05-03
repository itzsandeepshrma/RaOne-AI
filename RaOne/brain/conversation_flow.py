def update_context(user_input, response, old_context):
    old_context["last_input"] = user_input
    old_context["last_response"] = response
    return old_context
