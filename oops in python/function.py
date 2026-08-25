test_settings={
    'Theme':'light',
    'language':'english'
}

def add_setting(settings,t):
    key=t[0].lower()
    value=t[1].lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    else:
        settings[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings,update_item):
    key=update_item[0].lower()
    value=update_item[1].lower()

    if key in settings:
        settings[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
    
def view_settings(settings):
    if not settings:
        return "No settings available."
    
    result = "Current User Settings:\n"
    # Sort keys to ensure consistent output order if required, though dict order is preserved in modern Python
    for key in settings:
        # Capitalize the first letter of the key
        formatted_key = key.capitalize()
        result += f"{formatted_key}: {settings[key]}\n"
    
    return result

    