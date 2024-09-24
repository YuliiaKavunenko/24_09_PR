import flask

main_app = flask.Flask(
    import_name= "settings",
    template_folder= "main/templates"
)
