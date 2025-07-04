# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T17:49:41+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity
from fastapi import Path
from pydantic import conint

from models import (
    ApiV1GetResponse,
    ApiV1HolidaysGetResponse,
    ApiV1HolidaysHolidayIdGetResponse,
    ApiV1HolidaysHolidayIdGetResponse1,
    ApiV1ProvincesGetResponse,
    ApiV1ProvincesProvinceIdGetResponse,
    ApiV1ProvincesProvinceIdGetResponse1,
    Federal1,
    Optional1,
    ProvinceId,
)

app = MCPProxy(
    contact={
        'email': 'paul@pcraig3.ca',
        'name': 'Paul Craig',
        'url': 'https://canada-holidays.ca/api',
    },
    description='This API lists all 31 public holidays for all 13 provinces and territories in Canada, including federal holidays.',
    license={'name': 'MIT', 'url': 'https://github.com/pcraig3/hols/blob/main/LICENSE'},
    title='Canada Holidays API',
    version='1.8.0',
    servers=[{'url': 'https://canada-holidays.ca'}],
)


@app.get(
    '/api/v1',
    description=""" Returns a welcome message. """,
    tags=['holiday_data_operations'],
)
def root():
    """
    root
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/holidays',
    description=""" Returns Canadian public holidays. Each holiday lists the regions that observe it. """,
    tags=['holiday_data_operations'],
)
def holidays(
    year: Optional[conint(ge=2016, le=2029)] = 2023,
    federal: Optional[Federal1] = None,
    optional: Optional[Optional1] = 'false',
):
    """
    Get all holidays
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/holidays/{holidayId}',
    description=""" Returns one Canadian statutory holiday by integer id. Returns a 404 response for invalid ids. """,
    tags=['holiday_data_operations'],
)
def holiday(
    year: Optional[conint(ge=2016, le=2029)] = 2023,
    optional: Optional[Optional1] = 'false',
    holiday_id: conint(ge=1, le=32) = Path(..., alias='holidayId'),
):
    """
    Get a holiday by id
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/provinces',
    description=""" Returns provinces and territories in Canada. Each province or territory lists its associated holidays. """,
    tags=['province_data_fetching'],
)
def provinces(
    year: Optional[conint(ge=2016, le=2029)] = 2023,
    optional: Optional[Optional1] = 'false',
):
    """
    Get all provinces
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/provinces/{provinceId}',
    description=""" Returns a Canadian province or territory with its associated holidays. Returns a 404 response for invalid abbreviations. """,
    tags=['province_data_fetching'],
)
def province(
    year: Optional[conint(ge=2016, le=2029)] = 2023,
    optional: Optional[Optional1] = 'false',
    province_id: ProvinceId = Path(..., alias='provinceId'),
):
    """
    Get a province or territory by abbreviation
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/spec',
    description=""" Gets the schema for the JSON API as a yaml file. """,
    tags=['holiday_data_operations'],
)
def spec():
    """
    Get JSON schema
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
