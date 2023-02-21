#!/usr/bin/env python3

#  Copyright (c) 2014 INFN - "Istituto Nazionale di Fisica Nucleare" - Italy
#  All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License. 

from setuptools import setup
from setuptools import find_packages

setup(
    name='cloudveneto-horizon-extensions',
    version='1.2.7',
    description='CloudVeneto integrations for Openstack Horizon',
    long_description='''CloudVeneto integrations for Openstack Horizon''',
    license='Apache Software License',
    author_email='CloudVeneto <support@cloudveneto.it>',
    packages=find_packages(where="src"),
    package_dir = {'': 'src'},
    include_package_data=True
)


