[![NextCloud](https://nextcloud.com/media/nextcloud-logo.svg)](https://nextcloud.com/)

# Ansible Role - NextCloud deployment
Ansible Role to deploy NextCloud on a linux server.

[![Ansible Galaxy](https://img.shields.io/ansible/role/59111)](https://galaxy.ansible.com/ansibleguy/sw_nextcloud)
[![Ansible Galaxy Downloads](https://img.shields.io/badge/dynamic/json?color=blueviolet&label=Galaxy%20Downloads&query=%24.download_count&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F59111%2F%3Fformat%3Djson)](https://galaxy.ansible.com/ansibleguy/sw_nextcloud)

**Tested:**
* Debian 11


## Functionality

* **Package installation**
  * NextCloud Server
    * Dependencies (_php, ..._)
    * Apache2 => using [THIS Role](https://github.com/ansibleguy/infra_apache)
    * MariaDB => using [THIS Role](https://github.com/ansibleguy/infra_mariadb)


* **Configuration**
  * Default opt-ins:
    * Database setup
    * Webserver setup
    * Redis-server (_increased performance_)
    * PHP management

  * Default opt-outs:
    * Optional PHP modules
    * Admin-tools
    * Enhanced security config (_functionality might be impacted_)

  * Default config:
    * Logging to syslog
    * Upload size limit 20GB
    * Certificate signed by minimal CA

## Info

* **Note:** Most of this functionality can be opted in or out using the main defaults file and variables!


* **Note:** this role currently only supports debian-based systems


* **Info:** You can add custom config-overrides for PHP and the NextCloud by providing key-value pairs!

  PHP: ```nextcloud.php.cli/srv/fpm/fpm_pool```

  NextCloud: ```nextcloud.settings```


* **Note:** You can configure any target version of NextCloud to be installed!

  **BE AWARE that** the hardcoded dependencies might not work with all versions!


* **Disclaimer:** I'm not an expert regarding PHP-Setups - therefore some default settings might not be optimal.

  I copied it from the [official docker image](https://hub.docker.com/_/nextcloud/).

  If you have experience in that field => you are welcome to point out any possible optimizations. Just open an issue (:


* **Info:** You might need to add the server's certificate to your browser's exceptions if you use the 'selfsigned' or 'ca' certificate-type.


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
  enhanced_security: true
  tools: true  # install useful admin-tools
  
  php:  # php config-file overrides
    srv:
      timezone: 'Europe/Vienna'
  
  settings:  # nextcloud config-file overrides
    path_data: '/mnt/data'
    default_language: 'de'
    default_locale: 'de_DE'
    mail_from_address: 'nextcloud@template.ansibleguy.net'
    mail_smtphost: 'mail.template.ansibleguy.net'
  
  apache:
    domain: 'nextcloud.template.ansibleguy.net'
    aliases: ['nc.template.ansibleguy.net']
    ip: '192.168.0.100'  # else access via ip will be 'untrusted'

    ssl:
      mode: 'letsencrypt'  # or selfsigned/ca
      #  if you use 'selfsigned' or 'ca':
      #    cert:
      #      cn: 'NextCloud Server'
      #      org: 'AnsibleGuy'
      #      email: 'nextcloud@template.ansibleguy.net'
    letsencrypt:
      email: 'nextcloud@template.ansibleguy.net'
```

Bare minimum example:
```yaml
nextcloud:
  php:
    srv:
      timezone: 'Europe/Vienna'
  
  apache:
    domain: 'nextcloud.template.ansibleguy.net'
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
* certs
