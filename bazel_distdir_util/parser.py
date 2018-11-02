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

import re


GLOBAL_VARS_RE = re.compile(r"^\w+ =")
URL_RE = re.compile(r"https?://")
URL_VARS_RE = re.compile(r"urls? =")
QUOTE_RE = re.compile(r"\"\S+\"")


def parse_global_var(global_vars, line):
    m = GLOBAL_VARS_RE.search(line)
    if not m:
        return
    var_name = m.group().strip(" =")

    m = QUOTE_RE.search(line)
    if not m:
        return
    var_content = m.group().strip("\"")

    global_vars[var_name] = var_content


def parse_url(global_vars, urls, line):
    if not URL_RE.search(line):
        return
    if not URL_VARS_RE.search(line):
        return

    for var_name, var_content in global_vars.items():
        pattern = "\" + {} + \"".format(var_name)
        line = line.replace(pattern, var_content)

    m = QUOTE_RE.search(line)
    if not m:
        return
    url = m.group().strip("\"")

    urls.append(url)


def parse_urls(filename):
    global_vars = dict()
    urls = []

    with open(filename) as f:
        for line in f.readlines():
            parse_global_var(global_vars, line)
            parse_url(global_vars, urls, line)

    return urls
