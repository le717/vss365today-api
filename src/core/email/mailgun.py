from flask import current_app
import requests

__all__ = ["subscription_email_create", "subscription_email_delete"]


def subscription_email_create(addr: str) -> requests.Response:
    """Add a subscription email address."""
    # Construct the mailing list address. It is written this way
    # because the development and production lists are different
    # and we need to use the proper one depending on the env
    mg_list_addr = f'{current_app.config["MG_MAILING_LIST_ADDR"]}@{current_app.config["MG_DOMAIN"]}'

    return requests.post(
        f"https://api.mailgun.net/v3/lists/{mg_list_addr}/members",
        auth=("api", current_app.config["MG_API_KEY"]),
        data={"upsert": True, "subscribed": True, "address": addr},
    )


def subscription_email_delete(addr: str) -> requests.Response:
    """Remove a subscription email address."""
    # Construct the mailing list address. It is written this way
    # because the development and production lists are different
    # and we need to use the proper one depending on the env
    mg_list_addr = f'{current_app.config["MG_MAILING_LIST_ADDR"]}@{current_app.config["MG_DOMAIN"]}'

    return requests.delete(
        f"https://api.mailgun.net/v3/lists/{mg_list_addr}/members/{addr}",
        auth=("api", current_app.config["MG_API_KEY"]),
    )
