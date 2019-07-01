
THIS IS VERY MUCH A WORK IN PROGRESS

There are a whole host of sanic swagger projects out there:

 - https://github.com/huge-success/sanic-openapi From author of sanic
 - https://github.com/abatilo/sanic-swagger A fork of the above with added c/attrs support
 - https://github.com/yunstanford/sanic-transmute From the author of pytest-sanic amongst many other things

None of which as far as I can tell support OpenAPI spec 3.0, although I think sanic-transmute does partially. All of which seem to be focussed on dynamic documentation, rather than simply rendering a swagger json as per flask-swagger-ui. 

Or just use this directly?
- https://github.com/swagger-api/swagger-ui


TODO:
Conver flask_swagger_ui.py to use app.static instead of send_from_directory and use jinja2 templating directly


# flask-swagger-ui

Simple Flask blueprint for adding [Swagger UI](https://github.com/swagger-api/swagger-ui) to your flask application.

Included Swagger UI version: 3.20.9.

## Installation

`pip install flask-swagger-ui`

## Usage

Example application:

```python
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

# Register blueprint at URL
# (URL must match the one given to factory function above)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.run()

# Now point your browser to localhost:5000/api/docs/

```

## Configuration

The blueprint supports overloading all Swagger UI configuration options that can be JSON serialized.
See https://github.com/swagger-api/swagger-ui#parameters for options.

Plugins and function parameters are not supported at this time.

OAuth2 parameters can be found at https://github.com/swagger-api/swagger-ui#oauth2-configuration .
