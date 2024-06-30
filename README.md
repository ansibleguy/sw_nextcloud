[![NextCloud](https://nextcloud.com/media/nextcloud-logo.svg)](https://nextcloud.com/)

# Ansible Role - NextCloud Dockerized
Ansible Role to deploy dockerized NextCloud on a linux server.

<a href='https://ko-fi.com/ansible0guy' target='_blank'><img height='35' style='border:0px;height:46px;' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy me a coffee' />

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

## Usage

You want a simple Ansible GUI? Check-out my [Ansible WebUI](https://github.com/ansibleguy/webui)

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
