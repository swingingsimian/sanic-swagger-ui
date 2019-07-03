import os
import json

from jinja2 import Environment, PackageLoader, select_autoescape
from sanic import Blueprint, request, response

env = Environment(loader=PackageLoader('sanic_swagger_ui', 'templates'),
                  autoescape=select_autoescape(['html']))


def get_swaggerui_blueprint(
        base_url,
        api_url,
        config=None,
        #oauth_config=None,
        blueprint_name='swagger_ui'
):

    swagger_ui = Blueprint(blueprint_name,
                           base_url)

    default_config = {
        'app_name': 'Swagger UI',
        'dom_id': '#swagger-ui',
        'url': api_url,
        'layout': 'StandaloneLayout'
    }

    if config:
        default_config.update(config)

    fields = {
        # Some fields are used directly in template
        'base_url': f"{base_url}/static",
        'app_name': default_config.pop('app_name'),
        # Rest are just serialized into json string for inclusion in the .js file
        'config_json': json.dumps(default_config),

    }
    #if oauth_config:
    #    fields['oauth_config_json'] = json.dumps(oauth_config)

    swagger_ui.static('/static', f"{os.path.dirname(os.path.realpath(__file__))}/dist")

    @swagger_ui.route('/')
    def serve_swagger_template(request):
        #if not default_config.get('oauth2RedirectUrl', None):
        #    default_config.update(
        #        {"oauth2RedirectUrl": os.path.join(request.base_url, "oauth2-redirect.html")}
        #    )
        #    fields['config_json'] = json.dumps(default_config)

        template = env.get_template('index.template.html')
        return response.html(template.render(**fields))

    return swagger_ui

