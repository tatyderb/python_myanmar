import pytest

@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = request.param
    print(f"setup {smtp_connection}")
    yield smtp_connection
    print(f"finalizing {smtp_connection}")
