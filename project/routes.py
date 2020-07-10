def register_routes(api, app, root="api"):
    from project.core import register_routes as attach_app


    # Add routes
    attach_app(api, app)
