from ansible.module_utils.basic import AnsibleModule

def main():
    parameters = {
        'path': {"required": False, "type": 'str'},
        'before': {"required": True, "type": 'str'},
        'after': {"required": True, "type": 'str'},
        'cisid': {"required": True, "type": 'str'}
    }

    module = AnsibleModule(argument_spec=parameters)

    path = module.params['path']
    before = module.params['before']
    after = module.params['after']
    cisid = module.params['cisid']

    # output = cisid + path + before + after

    output = {
        'path': path,
        'before': before,
        'after': after,
        'cisid': cisid
    }

    module.exit_json(changed=False, **output)

if __name__ == '__main__':
    main()
