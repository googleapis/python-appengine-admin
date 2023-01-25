# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from typing import MutableMapping, MutableSequence

from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.appengine.v1",
    manifest={
        "ManagementStatus",
        "AuthorizedCertificate",
        "CertificateRawData",
        "ManagedCertificate",
    },
)


class ManagementStatus(proto.Enum):
    r"""State of certificate management. Refers to the most recent
    certificate acquisition or renewal attempt.

    Values:
        MANAGEMENT_STATUS_UNSPECIFIED (0):
            No description available.
        OK (1):
            Certificate was successfully obtained and
            inserted into the serving system.
        PENDING (2):
            Certificate is under active attempts to
            acquire or renew.
        FAILED_RETRYING_NOT_VISIBLE (4):
            Most recent renewal failed due to an invalid
            DNS setup and will be retried. Renewal attempts
            will continue to fail until the certificate
            domain's DNS configuration is fixed. The last
            successfully provisioned certificate may still
            be serving.
        FAILED_PERMANENT (6):
            All renewal attempts have been exhausted,
            likely due to an invalid DNS setup.
        FAILED_RETRYING_CAA_FORBIDDEN (7):
            Most recent renewal failed due to an explicit
            CAA record that does not include one of the
            in-use CAs (Google CA and Let's Encrypt).
            Renewals will continue to fail until the CAA is
            reconfigured. The last successfully provisioned
            certificate may still be serving.
        FAILED_RETRYING_CAA_CHECKING (8):
            Most recent renewal failed due to a CAA
            retrieval failure. This means that the domain's
            DNS provider does not properly handle CAA
            records, failing requests for CAA records when
            no CAA records are defined. Renewals will
            continue to fail until the DNS provider is
            changed or a CAA record is added for the given
            domain. The last successfully provisioned
            certificate may still be serving.
    """
    MANAGEMENT_STATUS_UNSPECIFIED = 0
    OK = 1
    PENDING = 2
    FAILED_RETRYING_NOT_VISIBLE = 4
    FAILED_PERMANENT = 6
    FAILED_RETRYING_CAA_FORBIDDEN = 7
    FAILED_RETRYING_CAA_CHECKING = 8


class AuthorizedCertificate(proto.Message):
    r"""An SSL certificate that a user has been authorized to
    administer. A user is authorized to administer any certificate
    that applies to one of their authorized domains.

    Attributes:
        name (str):
            Full path to the ``AuthorizedCertificate`` resource in the
            API. Example: ``apps/myapp/authorizedCertificates/12345``.

            @OutputOnly
        id (str):
            Relative name of the certificate. This is a unique value
            autogenerated on ``AuthorizedCertificate`` resource
            creation. Example: ``12345``.

            @OutputOnly
        display_name (str):
            The user-specified display name of the certificate. This is
            not guaranteed to be unique. Example: ``My Certificate``.
        domain_names (MutableSequence[str]):
            Topmost applicable domains of this certificate. This
            certificate applies to these domains and their subdomains.
            Example: ``example.com``.

            @OutputOnly
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when this certificate expires. To update the
            renewal time on this certificate, upload an SSL certificate
            with a different expiration time using
            ```AuthorizedCertificates.UpdateAuthorizedCertificate`` <>`__.

            @OutputOnly
        certificate_raw_data (google.cloud.appengine_admin_v1.types.CertificateRawData):
            The SSL certificate serving the ``AuthorizedCertificate``
            resource. This must be obtained independently from a
            certificate authority.
        managed_certificate (google.cloud.appengine_admin_v1.types.ManagedCertificate):
            Only applicable if this certificate is managed by App
            Engine. Managed certificates are tied to the lifecycle of a
            ``DomainMapping`` and cannot be updated or deleted via the
            ``AuthorizedCertificates`` API. If this certificate is
            manually administered by the user, this field will be empty.

            @OutputOnly
        visible_domain_mappings (MutableSequence[str]):
            The full paths to user visible Domain Mapping resources that
            have this certificate mapped. Example:
            ``apps/myapp/domainMappings/example.com``.

            This may not represent the full list of mapped domain
            mappings if the user does not have ``VIEWER`` permissions on
            all of the applications that have this certificate mapped.
            See ``domain_mappings_count`` for a complete count.

            Only returned by ``GET`` or ``LIST`` requests when
            specifically requested by the ``view=FULL_CERTIFICATE``
            option.

            @OutputOnly
        domain_mappings_count (int):
            Aggregate count of the domain mappings with this certificate
            mapped. This count includes domain mappings on applications
            for which the user does not have ``VIEWER`` permissions.

            Only returned by ``GET`` or ``LIST`` requests when
            specifically requested by the ``view=FULL_CERTIFICATE``
            option.

            @OutputOnly
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    domain_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    certificate_raw_data: "CertificateRawData" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="CertificateRawData",
    )
    managed_certificate: "ManagedCertificate" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="ManagedCertificate",
    )
    visible_domain_mappings: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    domain_mappings_count: int = proto.Field(
        proto.INT32,
        number=9,
    )


class CertificateRawData(proto.Message):
    r"""An SSL certificate obtained from a certificate authority.

    Attributes:
        public_certificate (str):
            PEM encoded x.509 public key certificate. This field is set
            once on certificate creation. Must include the header and
            footer. Example:

            .. raw:: html

                <pre>
                -----BEGIN CERTIFICATE-----
                <certificate_value>
                -----END CERTIFICATE-----
                </pre>
        private_key (str):
            Unencrypted PEM encoded RSA private key. This field is set
            once on certificate creation and then encrypted. The key
            size must be 2048 bits or fewer. Must include the header and
            footer. Example:

            .. raw:: html

                <pre>
                -----BEGIN RSA PRIVATE KEY-----
                <unencrypted_key_value>
                -----END RSA PRIVATE KEY-----
                </pre>

            @InputOnly
    """

    public_certificate: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ManagedCertificate(proto.Message):
    r"""A certificate managed by App Engine.

    Attributes:
        last_renewal_time (google.protobuf.timestamp_pb2.Timestamp):
            Time at which the certificate was last renewed. The renewal
            process is fully managed. Certificate renewal will
            automatically occur before the certificate expires. Renewal
            errors can be tracked via ``ManagementStatus``.

            @OutputOnly
        status (google.cloud.appengine_admin_v1.types.ManagementStatus):
            Status of certificate management. Refers to
            the most recent certificate acquisition or
            renewal attempt.
            @OutputOnly
    """

    last_renewal_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    status: "ManagementStatus" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ManagementStatus",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
