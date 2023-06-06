from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    
    # Blog Routes
    Route.get("/blog", "BlogController@show"),
]
