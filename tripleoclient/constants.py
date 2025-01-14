#   Copyright 2015 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

WEBROOT = '/dashboard/'

SERVICE_LIST = {
    'ceilometer': {'password_field': 'OVERCLOUD_CEILOMETER_PASSWORD'},
    'cinder': {'password_field': 'OVERCLOUD_CINDER_PASSWORD'},
    'cinderv2': {'password_field': 'OVERCLOUD_CINDER_PASSWORD'},
    'glance': {'password_field': 'OVERCLOUD_GLANCE_PASSWORD'},
    'heat': {'password_field': 'OVERCLOUD_HEAT_PASSWORD'},
    'neutron': {'password_field': 'OVERCLOUD_NEUTRON_PASSWORD'},
    'nova': {'password_field': 'OVERCLOUD_NOVA_PASSWORD'},
    'novav3': {'password_field': 'OVERCLOUD_NOVA_PASSWORD'},
    'swift': {'password_field': 'OVERCLOUD_SWIFT_PASSWORD'},
    'horizon': {
        'port': '80',
        'path': WEBROOT,
        'admin_path': '%sadmin' % WEBROOT},
}

TRIPLEO_HEAT_TEMPLATES = "/usr/share/openstack-tripleo-heat-templates/"
OVERCLOUD_YAML_NAME = "overcloud-without-mergepy.yaml"
RESOURCE_REGISTRY_NAME = "overcloud-resource-registry-puppet.yaml"
RHEL_REGISTRATION_EXTRACONFIG_NAME = (
    "extraconfig/post_deploy/rhel-registration/")

PARAMETERS = {
    'BlockStorageImage': 'overcloud-full',
    'CephStorageImage': 'overcloud-full',
    'CinderISCSIHelper': 'lioadm',
    'CloudName': 'overcloud',
    'controllerImage': 'overcloud-full',
    'NeutronNetworkVLANRanges': 'datacentre:1:1000',
    'NovaImage': 'overcloud-full',
    'OvercloudControlFlavor': 'baremetal',
    'OvercloudComputeFlavor': 'baremetal',
    'OvercloudBlockStorageFlavor': 'baremetal',
    'OvercloudSwiftStorageFlavor': 'baremetal',
    'OvercloudCephStorageFlavor': 'baremetal',
    'SwiftStorageImage': 'overcloud-full',
}

NEW_STACK_PARAMETERS = {
    'NovaComputeLibvirtType': 'kvm',
}
