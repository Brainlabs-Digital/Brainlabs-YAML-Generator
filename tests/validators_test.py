import validators


def test_valid_email_prefix() -> None:
    assert validators.test_valid_email_prefix("james")
    assert validators.test_valid_email_prefix("james.f")
    assert not validators.test_valid_email_prefix("james@brainlabsdigital.com")


def test_valid_email_prefix_list() -> None:
    pass


def test_valid_client_id() -> None:
    pass


def test_valid_date() -> None:
    pass


def test_valid_urls() -> None:
    pass


def test_valid_url_list() -> None:
    pass


def test_valid_cron() -> None:
    pass


def test_valid_directory() -> None:
    pass