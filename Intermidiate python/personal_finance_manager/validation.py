def validate_required_text(text, field_name):
    if not text or not text.strip():
        return False, f"El campo {field_name} es obligatorio."
    return True, ""


def validate_amount(amount):
    try:
        numeric_amount = float(amount)
    except ValueError:
        return False, "El monto debe ser un numero valido."

    if numeric_amount <= 0:
        return False, "El monto debe ser mayor que cero."

    return True, ""


def validate_unique_category(category_name, existing_categories):
    existing_names = [category.name.lower() for category in existing_categories]
    if category_name.strip().lower() in existing_names:
        return False, "La categoria ya existe."
    return True, ""


def validate_category_form(category_name, existing_categories):
    is_valid, message = validate_required_text(category_name, "categoria")
    if not is_valid:
        return False, message

    return validate_unique_category(category_name, existing_categories)


def validate_transaction_form(title, amount, category):
    is_valid, message = validate_required_text(title, "titulo")
    if not is_valid:
        return False, message

    is_valid, message = validate_amount(amount)
    if not is_valid:
        return False, message

    is_valid, message = validate_required_text(category, "categoria")
    if not is_valid:
        return False, message

    return True, ""
