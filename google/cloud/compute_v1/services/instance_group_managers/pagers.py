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
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Sequence,
    Tuple,
    Optional,
    Iterator,
)

from google.cloud.compute_v1.types import compute


class AggregatedListPager:
    """A pager for iterating through ``aggregated_list`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.InstanceGroupManagerAggregatedList` object, and
    provides an ``__iter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``AggregatedList`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.InstanceGroupManagerAggregatedList`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., compute.InstanceGroupManagerAggregatedList],
        request: compute.AggregatedListInstanceGroupManagersRequest,
        response: compute.InstanceGroupManagerAggregatedList,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.AggregatedListInstanceGroupManagersRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.InstanceGroupManagerAggregatedList):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.AggregatedListInstanceGroupManagersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[compute.InstanceGroupManagerAggregatedList]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[Tuple[str, compute.InstanceGroupManagersScopedList]]:
        for page in self.pages:
            yield from page.items.items()

    def get(self, key: str) -> Optional[compute.InstanceGroupManagersScopedList]:
        return self._response.items.get(key)

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPager:
    """A pager for iterating through ``list`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.InstanceGroupManagerList` object, and
    provides an ``__iter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``List`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.InstanceGroupManagerList`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., compute.InstanceGroupManagerList],
        request: compute.ListInstanceGroupManagersRequest,
        response: compute.InstanceGroupManagerList,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.ListInstanceGroupManagersRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.InstanceGroupManagerList):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.ListInstanceGroupManagersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[compute.InstanceGroupManagerList]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[compute.InstanceGroupManager]:
        for page in self.pages:
            yield from page.items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListErrorsPager:
    """A pager for iterating through ``list_errors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.InstanceGroupManagersListErrorsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListErrors`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.InstanceGroupManagersListErrorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., compute.InstanceGroupManagersListErrorsResponse],
        request: compute.ListErrorsInstanceGroupManagersRequest,
        response: compute.InstanceGroupManagersListErrorsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.ListErrorsInstanceGroupManagersRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.InstanceGroupManagersListErrorsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.ListErrorsInstanceGroupManagersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[compute.InstanceGroupManagersListErrorsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[compute.InstanceManagedByIgmError]:
        for page in self.pages:
            yield from page.items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListManagedInstancesPager:
    """A pager for iterating through ``list_managed_instances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.InstanceGroupManagersListManagedInstancesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``managed_instances`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListManagedInstances`` requests and continue to iterate
    through the ``managed_instances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.InstanceGroupManagersListManagedInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., compute.InstanceGroupManagersListManagedInstancesResponse
        ],
        request: compute.ListManagedInstancesInstanceGroupManagersRequest,
        response: compute.InstanceGroupManagersListManagedInstancesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.ListManagedInstancesInstanceGroupManagersRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.InstanceGroupManagersListManagedInstancesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.ListManagedInstancesInstanceGroupManagersRequest(
            request
        )
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[compute.InstanceGroupManagersListManagedInstancesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[compute.ManagedInstance]:
        for page in self.pages:
            yield from page.managed_instances

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPerInstanceConfigsPager:
    """A pager for iterating through ``list_per_instance_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.InstanceGroupManagersListPerInstanceConfigsResp` object, and
    provides an ``__iter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPerInstanceConfigs`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.InstanceGroupManagersListPerInstanceConfigsResp`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., compute.InstanceGroupManagersListPerInstanceConfigsResp],
        request: compute.ListPerInstanceConfigsInstanceGroupManagersRequest,
        response: compute.InstanceGroupManagersListPerInstanceConfigsResp,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.ListPerInstanceConfigsInstanceGroupManagersRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.InstanceGroupManagersListPerInstanceConfigsResp):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.ListPerInstanceConfigsInstanceGroupManagersRequest(
            request
        )
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[compute.InstanceGroupManagersListPerInstanceConfigsResp]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[compute.PerInstanceConfig]:
        for page in self.pages:
            yield from page.items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
