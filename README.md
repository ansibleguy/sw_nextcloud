[![NextCloud](https://nextcloud.com/wp-content/themes/next/assets/img/logo/nextcloud-logo.svg)](https://nextcloud.com/)

# Ansible Role - NextCloud deployment
Ansible Role to deploy NextCloud on a linux server.

[![Ansible Galaxy](https://img.shields.io/ansible/role/59090)](https://galaxy.ansible.com/ansibleguy/sw_nextcloud)
[![Ansible Galaxy Downloads](https://img.shields.io/badge/dynamic/json?color=blueviolet&label=Galaxy%20Downloads&query=%24.download_count&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F59090%2F%3Fformat%3Djson)](https://galaxy.ansible.com/ansibleguy/sw_nextcloud)

**Tested:**
* None


## Functionality

* **Package installation**
  * NextCloud Server
    * Dependencies (_php, ..._)
    * Nginx => using [THIS Role](https://github.com/ansibleguy/infra_nginx)
    * MariaDB => using [THIS Role](https://github.com/ansibleguy/infra_mariadb)


* **Configuration**
  * TO BE CONTINUED

## Info

* **Warning:** THIS ROLE IS NOT YET IN A STABLE STATE!


## Setup
For this role to work - you must install its dependencies first:

```
ansible-galaxy install -r requirements.yml
```

## Usage

### Config

Define the nextcloud dictionary as needed.

```yaml
nextcloud:
  TO_BE_CONTINUED
```

You might want to use 'ansible-vault' to encrypt your passwords:
```bash
ansible-vault encrypt_string
```

### Execution

Run the playbook:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml --ask-vault-pass
```

There are also some useful **tags** available:
* config
* php
* db
