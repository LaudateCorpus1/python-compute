from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import path_template
from google.api_core import gapic_v1
from requests import __version__ as requests_version
from typing import Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.cloud.compute_v1.types import compute

from .base import InterconnectAttachmentsTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)

class InterconnectAttachmentsRestTransport(InterconnectAttachmentsTransport):
    """REST backend transport for InterconnectAttachments.

    The InterconnectAttachments API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """
    def __init__(self, *,
            host: str = 'compute.googleapis.com',
            credentials: ga_credentials.Credentials=None,
            credentials_file: str=None,
            scopes: Sequence[str]=None,
            client_cert_source_for_mtls: Callable[[
                ], Tuple[bytes, bytes]]=None,
            quota_project_id: Optional[str]=None,
            client_info: gapic_v1.client_info.ClientInfo=DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool]=False,
            url_scheme: str='https',
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._prep_wrapped_messages(client_info)

    __aggregated_list_required_fields_default_values =  {
        "project" : "",    }

    @staticmethod
    def _aggregated_list_get_unset_required_fields(message_dict):
        return {k: v for k, v in InterconnectAttachmentsRestTransport.__aggregated_list_required_fields_default_values.items() if k not in message_dict}

    def _aggregated_list(self,
            request: compute.AggregatedListInterconnectAttachmentsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: float=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> compute.InterconnectAttachmentAggregatedList:
        r"""Call the aggregated list method over HTTP.

        Args:
            request (~.compute.AggregatedListInterconnectAttachmentsRequest):
                The request object. A request message for
                InterconnectAttachments.AggregatedList.
                See the method description for details.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.InterconnectAttachmentAggregatedList:

        """

        http_options = [
            {
                'method': 'get',
                'uri': '/compute/v1/projects/{project}/aggregated/interconnectAttachments',
            },
        ]

        request_kwargs = compute.AggregatedListInterconnectAttachmentsRequest.to_dict(request)
        transcoded_request = path_template.transcode(
            http_options, **request_kwargs)

        uri = transcoded_request['uri']
        method = transcoded_request['method']

        # Jsonify the query params
        query_params = json.loads(compute.AggregatedListInterconnectAttachmentsRequest.to_json(
            compute.AggregatedListInterconnectAttachmentsRequest(transcoded_request['query_params']),
            including_default_value_fields=False,
            use_integers_for_enums=False
        ))

        query_params.update(self._aggregated_list_get_unset_required_fields(query_params))

        # Send the request
        headers = dict(metadata)
        headers['Content-Type'] = 'application/json'
        response=getattr(self._session, method)(
            # Replace with proper schema configuration (http/https) logic
            "https://{host}{uri}".format(host=self._host, uri=uri),
            timeout=timeout,
            headers=headers,
            params=rest_helpers.flatten_query_params(query_params),
        )

        # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
        # subclass.
        if response.status_code >= 400:
            raise core_exceptions.from_http_response(response)

        # Return the response
        return compute.InterconnectAttachmentAggregatedList.from_json(
            response.content,
            ignore_unknown_fields=True
        )

    __delete_required_fields_default_values =  {
        "interconnectAttachment" : "",        "project" : "",        "region" : "",    }

    @staticmethod
    def _delete_get_unset_required_fields(message_dict):
        return {k: v for k, v in InterconnectAttachmentsRestTransport.__delete_required_fields_default_values.items() if k not in message_dict}

    def _delete(self,
            request: compute.DeleteInterconnectAttachmentRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: float=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> compute.Operation:
        r"""Call the delete method over HTTP.

        Args:
            request (~.compute.DeleteInterconnectAttachmentRequest):
                The request object. A request message for
                InterconnectAttachments.Delete. See the
                method description for details.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.Operation:
                Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

        """

        http_options = [
            {
                'method': 'delete',
                'uri': '/compute/v1/projects/{project}/regions/{region}/interconnectAttachments/{interconnect_attachment}',
            },
        ]

        request_kwargs = compute.DeleteInterconnectAttachmentRequest.to_dict(request)
        transcoded_request = path_template.transcode(
            http_options, **request_kwargs)

        uri = transcoded_request['uri']
        method = transcoded_request['method']

        # Jsonify the query params
        query_params = json.loads(compute.DeleteInterconnectAttachmentRequest.to_json(
            compute.DeleteInterconnectAttachmentRequest(transcoded_request['query_params']),
            including_default_value_fields=False,
            use_integers_for_enums=False
        ))

        query_params.update(self._delete_get_unset_required_fields(query_params))

        # Send the request
        headers = dict(metadata)
        headers['Content-Type'] = 'application/json'
        response=getattr(self._session, method)(
            # Replace with proper schema configuration (http/https) logic
            "https://{host}{uri}".format(host=self._host, uri=uri),
            timeout=timeout,
            headers=headers,
            params=rest_helpers.flatten_query_params(query_params),
        )

        # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
        # subclass.
        if response.status_code >= 400:
            raise core_exceptions.from_http_response(response)

        # Return the response
        return compute.Operation.from_json(
            response.content,
            ignore_unknown_fields=True
        )

    __get_required_fields_default_values =  {
        "interconnectAttachment" : "",        "project" : "",        "region" : "",    }

    @staticmethod
    def _get_get_unset_required_fields(message_dict):
        return {k: v for k, v in InterconnectAttachmentsRestTransport.__get_required_fields_default_values.items() if k not in message_dict}

    def _get(self,
            request: compute.GetInterconnectAttachmentRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: float=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> compute.InterconnectAttachment:
        r"""Call the get method over HTTP.

        Args:
            request (~.compute.GetInterconnectAttachmentRequest):
                The request object. A request message for
                InterconnectAttachments.Get. See the
                method description for details.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.InterconnectAttachment:
                Represents an Interconnect Attachment
                (VLAN) resource. You can use
                Interconnect attachments (VLANS) to
                connect your Virtual Private Cloud
                networks to your on-premises networks
                through an Interconnect. For more
                information, read Creating VLAN
                Attachments.

        """

        http_options = [
            {
                'method': 'get',
                'uri': '/compute/v1/projects/{project}/regions/{region}/interconnectAttachments/{interconnect_attachment}',
            },
        ]

        request_kwargs = compute.GetInterconnectAttachmentRequest.to_dict(request)
        transcoded_request = path_template.transcode(
            http_options, **request_kwargs)

        uri = transcoded_request['uri']
        method = transcoded_request['method']

        # Jsonify the query params
        query_params = json.loads(compute.GetInterconnectAttachmentRequest.to_json(
            compute.GetInterconnectAttachmentRequest(transcoded_request['query_params']),
            including_default_value_fields=False,
            use_integers_for_enums=False
        ))

        query_params.update(self._get_get_unset_required_fields(query_params))

        # Send the request
        headers = dict(metadata)
        headers['Content-Type'] = 'application/json'
        response=getattr(self._session, method)(
            # Replace with proper schema configuration (http/https) logic
            "https://{host}{uri}".format(host=self._host, uri=uri),
            timeout=timeout,
            headers=headers,
            params=rest_helpers.flatten_query_params(query_params),
        )

        # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
        # subclass.
        if response.status_code >= 400:
            raise core_exceptions.from_http_response(response)

        # Return the response
        return compute.InterconnectAttachment.from_json(
            response.content,
            ignore_unknown_fields=True
        )

    __insert_required_fields_default_values =  {
        "project" : "",        "region" : "",    }

    @staticmethod
    def _insert_get_unset_required_fields(message_dict):
        return {k: v for k, v in InterconnectAttachmentsRestTransport.__insert_required_fields_default_values.items() if k not in message_dict}

    def _insert(self,
            request: compute.InsertInterconnectAttachmentRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: float=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> compute.Operation:
        r"""Call the insert method over HTTP.

        Args:
            request (~.compute.InsertInterconnectAttachmentRequest):
                The request object. A request message for
                InterconnectAttachments.Insert. See the
                method description for details.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.Operation:
                Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

        """

        http_options = [
            {
                'method': 'post',
                'uri': '/compute/v1/projects/{project}/regions/{region}/interconnectAttachments',
                'body': 'interconnect_attachment_resource',
            },
        ]

        request_kwargs = compute.InsertInterconnectAttachmentRequest.to_dict(request)
        transcoded_request = path_template.transcode(
            http_options, **request_kwargs)

        # Jsonify the request body
        body = compute.InterconnectAttachment.to_json(
            compute.InterconnectAttachment(
                transcoded_request['body']),
            including_default_value_fields=False,
            use_integers_for_enums=False
        )
        uri = transcoded_request['uri']
        method = transcoded_request['method']

        # Jsonify the query params
        query_params = json.loads(compute.InsertInterconnectAttachmentRequest.to_json(
            compute.InsertInterconnectAttachmentRequest(transcoded_request['query_params']),
            including_default_value_fields=False,
            use_integers_for_enums=False
        ))

        query_params.update(self._insert_get_unset_required_fields(query_params))

        # Send the request
        headers = dict(metadata)
        headers['Content-Type'] = 'application/json'
        response=getattr(self._session, method)(
            # Replace with proper schema configuration (http/https) logic
            "https://{host}{uri}".format(host=self._host, uri=uri),
            timeout=timeout,
            headers=headers,
            params=rest_helpers.flatten_query_params(query_params),
            data=body,
        )

        # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
        # subclass.
        if response.status_code >= 400:
            raise core_exceptions.from_http_response(response)

        # Return the response
        return compute.Operation.from_json(
            response.content,
            ignore_unknown_fields=True
        )

    __list_required_fields_default_values =  {
        "project" : "",        "region" : "",    }

    @staticmethod
    def _list_get_unset_required_fields(message_dict):
        return {k: v for k, v in InterconnectAttachmentsRestTransport.__list_required_fields_default_values.items() if k not in message_dict}

    def _list(self,
            request: compute.ListInterconnectAttachmentsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: float=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> compute.InterconnectAttachmentList:
        r"""Call the list method over HTTP.

        Args:
            request (~.compute.ListInterconnectAttachmentsRequest):
                The request object. A request message for
                InterconnectAttachments.List. See the
                method description for details.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.InterconnectAttachmentList:
                Response to the list request, and
                contains a list of interconnect
                attachments.

        """

        http_options = [
            {
                'method': 'get',
                'uri': '/compute/v1/projects/{project}/regions/{region}/interconnectAttachments',
            },
        ]

        request_kwargs = compute.ListInterconnectAttachmentsRequest.to_dict(request)
        transcoded_request = path_template.transcode(
            http_options, **request_kwargs)

        uri = transcoded_request['uri']
        method = transcoded_request['method']

        # Jsonify the query params
        query_params = json.loads(compute.ListInterconnectAttachmentsRequest.to_json(
            compute.ListInterconnectAttachmentsRequest(transcoded_request['query_params']),
            including_default_value_fields=False,
            use_integers_for_enums=False
        ))

        query_params.update(self._list_get_unset_required_fields(query_params))

        # Send the request
        headers = dict(metadata)
        headers['Content-Type'] = 'application/json'
        response=getattr(self._session, method)(
            # Replace with proper schema configuration (http/https) logic
            "https://{host}{uri}".format(host=self._host, uri=uri),
            timeout=timeout,
            headers=headers,
            params=rest_helpers.flatten_query_params(query_params),
        )

        # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
        # subclass.
        if response.status_code >= 400:
            raise core_exceptions.from_http_response(response)

        # Return the response
        return compute.InterconnectAttachmentList.from_json(
            response.content,
            ignore_unknown_fields=True
        )

    __patch_required_fields_default_values =  {
        "interconnectAttachment" : "",        "project" : "",        "region" : "",    }

    @staticmethod
    def _patch_get_unset_required_fields(message_dict):
        return {k: v for k, v in InterconnectAttachmentsRestTransport.__patch_required_fields_default_values.items() if k not in message_dict}

    def _patch(self,
            request: compute.PatchInterconnectAttachmentRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: float=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> compute.Operation:
        r"""Call the patch method over HTTP.

        Args:
            request (~.compute.PatchInterconnectAttachmentRequest):
                The request object. A request message for
                InterconnectAttachments.Patch. See the
                method description for details.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.compute.Operation:
                Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

        """

        http_options = [
            {
                'method': 'patch',
                'uri': '/compute/v1/projects/{project}/regions/{region}/interconnectAttachments/{interconnect_attachment}',
                'body': 'interconnect_attachment_resource',
            },
        ]

        request_kwargs = compute.PatchInterconnectAttachmentRequest.to_dict(request)
        transcoded_request = path_template.transcode(
            http_options, **request_kwargs)

        # Jsonify the request body
        body = compute.InterconnectAttachment.to_json(
            compute.InterconnectAttachment(
                transcoded_request['body']),
            including_default_value_fields=False,
            use_integers_for_enums=False
        )
        uri = transcoded_request['uri']
        method = transcoded_request['method']

        # Jsonify the query params
        query_params = json.loads(compute.PatchInterconnectAttachmentRequest.to_json(
            compute.PatchInterconnectAttachmentRequest(transcoded_request['query_params']),
            including_default_value_fields=False,
            use_integers_for_enums=False
        ))

        query_params.update(self._patch_get_unset_required_fields(query_params))

        # Send the request
        headers = dict(metadata)
        headers['Content-Type'] = 'application/json'
        response=getattr(self._session, method)(
            # Replace with proper schema configuration (http/https) logic
            "https://{host}{uri}".format(host=self._host, uri=uri),
            timeout=timeout,
            headers=headers,
            params=rest_helpers.flatten_query_params(query_params),
            data=body,
        )

        # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
        # subclass.
        if response.status_code >= 400:
            raise core_exceptions.from_http_response(response)

        # Return the response
        return compute.Operation.from_json(
            response.content,
            ignore_unknown_fields=True
        )

    @ property
    def aggregated_list(self) -> Callable[
            [compute.AggregatedListInterconnectAttachmentsRequest],
            compute.InterconnectAttachmentAggregatedList]:
        return self._aggregated_list
    @ property
    def delete(self) -> Callable[
            [compute.DeleteInterconnectAttachmentRequest],
            compute.Operation]:
        return self._delete
    @ property
    def get(self) -> Callable[
            [compute.GetInterconnectAttachmentRequest],
            compute.InterconnectAttachment]:
        return self._get
    @ property
    def insert(self) -> Callable[
            [compute.InsertInterconnectAttachmentRequest],
            compute.Operation]:
        return self._insert
    @ property
    def list(self) -> Callable[
            [compute.ListInterconnectAttachmentsRequest],
            compute.InterconnectAttachmentList]:
        return self._list
    @ property
    def patch(self) -> Callable[
            [compute.PatchInterconnectAttachmentRequest],
            compute.Operation]:
        return self._patch
    def close(self):
        self._session.close()


__all__=(
    'InterconnectAttachmentsRestTransport',
)
