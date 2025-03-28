# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "apic metadata update",
)
class Update(AAZCommand):
    """Update existing metadata schema.

    :example: Update schema
        az apic metadata update --resource-group api-center-test --service-name contoso --metadata-name "test1" --schema '{\"type\":\"string\", \"title\":\"Last name\", \"pattern\": \"^[a-zA-Z0-9]+$\"}'

    :example: Update schema using schema json file
        az apic metadata update --resource-group api-center-test --service-name contoso --metadata-name "test1" --schema '@schema.json'
    """

    _aaz_info = {
        "version": "2024-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.apicenter/services/{}/metadataschemas/{}", "2024-03-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.metadata_name = AAZStrArg(
            options=["--metadata-name"],
            help="The name of the metadata schema.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.service_name = AAZStrArg(
            options=["-n", "--service-name"],
            help="The name of Azure API Center service.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.assignments = AAZListArg(
            options=["--assignments"],
            arg_group="Properties",
            help="Defines the assignment scope for the custom metadata, e.g. \"[{entity:api,required:true,deprecated:false}]\". The available entity values are: api, deployment, environment.",
            nullable=True,
        )
        _args_schema.schema = AAZStrArg(
            options=["--schema"],
            arg_group="Properties",
            help="YAML schema defining the type.",
        )

        assignments = cls._args_schema.assignments
        assignments.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.assignments.Element
        _element.deprecated = AAZBoolArg(
            options=["deprecated"],
            help="Deprecated assignment",
            nullable=True,
        )
        _element.entity = AAZStrArg(
            options=["entity"],
            help="The entities this metadata schema component gets applied to.",
            nullable=True,
            enum={"api": "api", "deployment": "deployment", "environment": "environment"},
        )
        _element.required = AAZBoolArg(
            options=["required"],
            help="Required assignment",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.MetadataSchemasGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.MetadataSchemasCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class MetadataSchemasGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiCenter/services/{serviceName}/metadataSchemas/{metadataSchemaName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "metadataSchemaName", self.ctx.args.metadata_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceName", self.ctx.args.service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_metadata_schema_read(cls._schema_on_200)

            return cls._schema_on_200

    class MetadataSchemasCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiCenter/services/{serviceName}/metadataSchemas/{metadataSchemaName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "metadataSchemaName", self.ctx.args.metadata_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceName", self.ctx.args.service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_metadata_schema_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("assignedTo", AAZListType, ".assignments")
                properties.set_prop("schema", AAZStrType, ".schema", typ_kwargs={"flags": {"required": True}})

            assigned_to = _builder.get(".properties.assignedTo")
            if assigned_to is not None:
                assigned_to.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.assignedTo[]")
            if _elements is not None:
                _elements.set_prop("deprecated", AAZBoolType, ".deprecated")
                _elements.set_prop("entity", AAZStrType, ".entity")
                _elements.set_prop("required", AAZBoolType, ".required")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_metadata_schema_read = None

    @classmethod
    def _build_schema_metadata_schema_read(cls, _schema):
        if cls._schema_metadata_schema_read is not None:
            _schema.id = cls._schema_metadata_schema_read.id
            _schema.name = cls._schema_metadata_schema_read.name
            _schema.properties = cls._schema_metadata_schema_read.properties
            _schema.system_data = cls._schema_metadata_schema_read.system_data
            _schema.type = cls._schema_metadata_schema_read.type
            return

        cls._schema_metadata_schema_read = _schema_metadata_schema_read = AAZObjectType()

        metadata_schema_read = _schema_metadata_schema_read
        metadata_schema_read.id = AAZStrType(
            flags={"read_only": True},
        )
        metadata_schema_read.name = AAZStrType(
            flags={"read_only": True},
        )
        metadata_schema_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        metadata_schema_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        metadata_schema_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_metadata_schema_read.properties
        properties.assigned_to = AAZListType(
            serialized_name="assignedTo",
        )
        properties.schema = AAZStrType(
            flags={"required": True},
        )

        assigned_to = _schema_metadata_schema_read.properties.assigned_to
        assigned_to.Element = AAZObjectType()

        _element = _schema_metadata_schema_read.properties.assigned_to.Element
        _element.deprecated = AAZBoolType()
        _element.entity = AAZStrType()
        _element.required = AAZBoolType()

        system_data = _schema_metadata_schema_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_metadata_schema_read.id
        _schema.name = cls._schema_metadata_schema_read.name
        _schema.properties = cls._schema_metadata_schema_read.properties
        _schema.system_data = cls._schema_metadata_schema_read.system_data
        _schema.type = cls._schema_metadata_schema_read.type


__all__ = ["Update"]
