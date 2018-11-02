#!/usr/bin/env python

# Copyright (C) 2018 SUSE LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid

try:  # for pip >= 10
    from pip._internal import req as pip_req
except ImportError:  # for pip <= 9.0.3
    from pip import req as pip_req
import setuptools


install_reqs = pip_req.parse_requirements('requirements.txt', session=uuid.uuid1())
requirements = [str(req.req) for req in install_reqs]

setuptools.setup(
    name='bazel-distdir-util',
    version='0.1.0',
    description='Utility for pre-fetching dependencies for Bazel',
    author='Michal Rostecki',
    author_email='mrostecki@suse.de',
    url='https://github.com/mrostecki/bazel-distdir-util',
    packages=['bazel_distdir_util'],
    entry_points={
        'console_scripts': [
            'bazel-distdir-util = bazel_distdir_util.__main__:main',
        ]
    },
    install_requires=requirements,
    license='Apache-2.0',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: System :: Systems Administration',
    ],
)
