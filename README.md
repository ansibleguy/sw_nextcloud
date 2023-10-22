[![NextCloud](https://nextcloud.com/media/nextcloud-logo.svg)](https://nextcloud.com/)

# Ansible Role - NextCloud deployment
Ansible Role to deploy NextCloud on a linux server.

[![Molecule Test Status](https://badges.ansibleguy.net/sw_nextcloud.molecule.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/molecule.sh.j2)
[![YamlLint Test Status](https://badges.ansibleguy.net/sw_nextcloud.yamllint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/yamllint.sh.j2)
[![PyLint Test Status](https://badges.ansibleguy.net/sw_nextcloud.pylint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/pylint.sh.j2)
[![Ansible-Lint Test Status](https://badges.ansibleguy.net/sw_nextcloud.ansiblelint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/ansiblelint.sh.j2)
[![Ansible Galaxy](https://badges.ansibleguy.net/galaxy.badge.svg)](https://galaxy.ansible.com/ui/standalone/roles/ansibleguy/sw_nextcloud)

**Tested:**
* Debian 11

## Install

```bash
ansible-galaxy install ansibleguy.sw_nextcloud

# or to custom role-path
ansible-galaxy install ansibleguy.sw_nextcloud --roles-path ./roles

# install dependencies
ansible-galaxy install -r requirements.yml
```

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

* **Note:** Most of the role's functionality can be opted in or out.

  For all available options - see the default-config located in the main defaults-file!


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


* **Info:** The machine running NextCloud should AT LEAST have 1GB of RAM to run somewhat OK.

  2-4GB would be recommended for entry-level setups. You might want/have to update the php memory-limit ```nextcloud.php.srv.memory_limit```if you have more than 1GB available!


## Usage

### Config

Define the nextcloud dictionary as needed.

```yaml
nextcloud:
  enhanced_security: true
  tools: true  # install useful admin-tools

  # version: '24.0.3'
  # upgrade: true => set to upgrade to newer version
  
  php:  # php config-file overrides
    srv:
      timezone: 'Europe/Vienna'
      memory_limit: '2G'
      post_max_size: '200G'
      upload_max_filesize: '200G'
  
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
