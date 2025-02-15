[![NextCloud](https://nextcloud.com/media/nextcloud-logo.svg)](https://nextcloud.com/)

# Ansible Role - NextCloud Dockerized
Ansible Role to deploy dockerized NextCloud on a linux server.

[![Lint](https://github.com/ansibleguy/sw_nextcloud/actions/workflows/lint.yml/badge.svg)](https://github.com/ansibleguy/sw_nextcloud/actions/workflows/lint.yml)
[![Ansible Galaxy](https://badges.ansibleguy.net/galaxy.badge.svg)](https://galaxy.ansible.com/ui/standalone/roles/ansibleguy/sw_nextcloud)

**Molecule Integration-Tests**:

* Status: [![Molecule Test Status](https://badges.ansibleguy.net/sw_nextcloud.molecule.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/molecule.sh.j2) |
[![Functional-Tests](https://github.com/ansibleguy/sw_nextcloud/actions/workflows/integration_test_result.yml/badge.svg)](https://github.com/ansibleguy/sw_nextcloud/actions/workflows/integration_test_result.yml)
* Logs: [API](https://ci.ansibleguy.net/api/job/ansible-test-molecule-sw_nextcloud/logs?token=2b7bba30-9a37-4b57-be8a-99e23016ce70&lines=1000) | [Short](https://badges.ansibleguy.net/log/molecule_sw_nextcloud_test_short.log) | [Full](https://badges.ansibleguy.net/log/molecule_sw_nextcloud_test.log)

Internal CI: [Tester Role](https://github.com/ansibleguy/_meta_cicd) | [Jobs API](https://github.com/O-X-L/github-self-hosted-jobs-systemd)

**Tested:**
* Debian 12

----

## Install

```bash
# latest
ansible-galaxy role install git+https://github.com/ansibleguy/sw_nextcloud

# from galaxy
ansible-galaxy install ansibleguy.sw_nextcloud

# or to custom role-path
ansible-galaxy install ansibleguy.sw_nextcloud --roles-path ./roles

# install dependencies
ansible-galaxy install -r requirements.yml
```

----

## Advertisement

* Need **professional support** using Ansible or NextCloud? Contact us:

  E-Mail: [contact@oxl.at](mailto:contact@oxl.at)

  Tel: [+43 3115 40 900 0](tel:+433115409000)

  Web: [EN](https://www.o-x-l.com) | [DE](https://www.oxl.at)

  Language: German or English

* You want a simple **Ansible GUI**?

  Check-out this [Ansible WebUI](https://github.com/ansibleguy/webui)

----

## Usage

### Config

Minimum example:
```yaml
nextcloud:
  hostnames: ['nextcloud.template.ansibleguy.net']
```

Define the nextcloud dictionary as needed.

```yaml
nextcloud:
  hostnames: ['nextcloud.template.ansibleguy.net']
  admin:
    pwd: !vault |
      ...
  db:
    app_pwd: !vault |
      ...
    root_pwd: !vault |
      ...
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
* webserver
* docker

----


## Functionality

* **Package installation**
  * Ansible dependencies (_minimal_)
  * Docker server and client
  * Nginx if webserver is managed


* **Configuration**

  * **Default config**:
    * Using MariaDB database

  * **Default opt-ins**:
    * Auto-Update Job
    * Managing Webserver => see: [THIS Role](https://github.com/ansibleguy/infra_nginx)


## Info

* **Note:** Most of the role's functionality can be opted in or out.

  For all available options - see the default-config located in [the main defaults-file](https://github.com/ansibleguy/sw_nextcloud/blob/latest/defaults/main/1_main.yml)!


* **Note:** this role currently only supports debian-based systems


* **Info:** The machine running NextCloud should AT LEAST have 4GB of RAM to run somewhat OK.
