"""Just for starting the application."""

from src.main_application import MainApplication

# nur main page kann ausgeführt werden, die anderen nicht
if __name__ == "__main__":
    # Entrypoint for the application.
    app = MainApplication()
    app.mainloop()
