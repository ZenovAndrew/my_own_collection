#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: create_file
short_description: Create some file with content
# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"
description: This is test module, module creates txt files with content
options:
    path:
        description: Full path to file
        required: true
        type: str
    content:
        description: File content
        required: true
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - ansible.modules.create
author:
    - Zenov Andrew (https://github.com/ZenovAndrew)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.create_file:
    path: "/tmp/simple_file.txt"
    content: "enter your content"
    new: true
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: "your content"
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'File created'
'''

from os import path
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=True,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    if not path.exists(module.params['path']):
        with open(module.params['path'], 'w') as new_file:
            new_file.write(module.params['content'])
        result['changed'] = True
        result['message'] = 'File created'
    else:
        result['changed'] = False
        result['message'] = "File alreadey exist"

    result['message'] = module.params['content']

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
	
