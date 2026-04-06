from urllib.parse import quote

from django.conf import settings


def whatsapp(request):
    """
    Expose wa.me link for templates when WHATSAPP_PHONE_NUMBER is set.
    Phone may include spaces, +, dashes; only digits are sent to WhatsApp.
    """
    raw = getattr(settings, 'WHATSAPP_PHONE_NUMBER', '') or ''
    digits = ''.join(c for c in str(raw) if c.isdigit())
    if not digits:
        return {'whatsapp_chat_url': ''}

    url = f'https://wa.me/{digits}'
    msg = (getattr(settings, 'WHATSAPP_PREFILL_MESSAGE', '') or '').strip()
    if msg:
        url = f'{url}?text={quote(msg)}'
    return {'whatsapp_chat_url': url}
