"""Dummy flask API to generate the OpenAPI Specification
including the schemas in dracor_api_response_schemas.py"""

import flask
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
import json
from dracor_api_response_schemas import InfoSchema, CorpusInCorporaSchema


# Setup of flask API
api = flask.Flask(__name__)
# enable UTF-8 support
api.config["JSON_AS_ASCII"] = False


@api.route("/info", methods=["GET"])
def get_info():
    """
    ---
    get:
      summary: API info
      description: >-
        Shows version numbers of the dracor-api app and the underlying
        eXist-db.
      operationId: api-info
      tags: [public]
      responses:
        '200':
          description: Returns JSON object
          content:
            application/json:
                schema: InfoSchema
    """
    pass


@api.route("/corpora", methods=["GET"])
def get_corpora():
    """
    ---
    get:
      summary: List available corpora
      operationId: list-corpora
      tags: [public]
      parameters:
        - name: include
          in: query
          description: Include metrics for each corpus
          required: false
          schema:
            type: string
            enum: [metrics]
      responses:
        '200':
          description: Returns list of available corpora
          content:
            application/json:
              schema:
                type: array
                items:
                  schema: CorpusInCorporaSchema
    """


spec = APISpec(
    title="DraCor API",
    version="0.83.1",
    openapi_version="3.0.3",
    info=dict(
        contact=dict(
            email="fr.fischer@fu-berlin.de"
        ),
        termsOfService = "https://dracor.org",
        license=dict(
            name="Apache 2.0",
            url="http://www.apache.org/licenses/LICENSE-2.0.html"
        )
    ),
    servers=[
        dict(
            description="Production",
            url="https://dracor.org/api"
        )
    ],
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

# Generate the OpenAPI Specification
with api.test_request_context():
    spec.path(view=get_info)
    spec.path(view=get_corpora)


# write the OpenAPI Specification as YAML to the root folder
with open('dracor_api_openapi.yaml', 'w') as f:
    f.write(spec.to_yaml())

# Write the Specification as JSON to the root folder
with open('dracor_api_openapi.json', 'w') as f:
    json.dump(spec.to_dict(), f)

