from fastapi import FastAPI
from nicegui import ui

from .login import login_page
from .main import main_page


def init(fastapi_app: FastAPI) -> None:
    @ui.page("/")
    def home():
        main_page()

    @ui.page("/login")
    def login():
        login_page()

    ui.run_with(
        fastapi_app,
        mount_path="/",  # NOTE this can be omitted if you want the paths passed to @ui.page to be at the root
        storage_secret="pick your private secret here",  # NOTE setting a secret is optional but allows for persistent storage per user # noqa
    )
