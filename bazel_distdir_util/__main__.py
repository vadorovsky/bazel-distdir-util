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

from __future__ import print_function
import argparse
import sys

from bazel_distdir_util import find
from bazel_distdir_util import parser


def print_urls(urls, rpm_format=False):
    for no, url in enumerate(urls):
        if rpm_format:
            url = "Source{}: {}".format(no + 1, url)
        print(url)


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--rpmspec-format', action='store_true')
    args = argparser.parse_args()

    bzl_files = find.find_bzl_files()

    if not bzl_files:
        print("Could not found any *.bzl files", file=sys.stderr)
        sys.exit(1)

    urls = []
    for bzl_file in bzl_files:
        urls += parser.parse_urls(bzl_file)
    print_urls(urls, rpm_format=args.rpmspec_format)


if __name__ == '__main__':
    main()
