from app import create_app


app = create_app()


if __name__ == "__main__":
    from werkzeug.serving import run_simple

    run_simple(hostname="localhost", port=6502, application=app, use_reloader=True, use_debugger=True)
