from django.core.exceptions import ValidationError


def validate_phone(phone):
    phone_length = len(phone)

    if phone_length < 10:
        raise ValidationError(
            f'{phone} is not a valid phone number, the size must be 10 or 11.',
            params={'phone': phone},
        )

def validate_cpf_len(cpf):
    cpf_length = len(cpf)

    if cpf_length < 11:
        raise ValidationError(
            f'{cpf} is not a valid CPF',
            params={'cpf': cpf},
        )
