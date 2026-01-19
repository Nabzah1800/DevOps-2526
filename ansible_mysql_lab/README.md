# ansible_mysql_lab

Deze map bevat een Ansible lab voor het installeren en configureren van een MySQL database server.

## Bestanden
- **ansible.cfg**: Ansible configuratiebestand.
- **mysql.yml**: Playbook voor het installeren en configureren van MySQL.
- **configure_ssh_server.sh**: Script om SSH server te configureren.
- **hosts**: Inventarisbestand met de doelhosts.

## Wat doet dit playbook?

Dit Ansible playbook installeert en configureert automatisch een MySQL database server met de volgende stappen:

1. **MySQL Server Installatie**: Installeert MySQL server en Python MySQL bibliotheek
2. **Service Management**: Start en enabled MySQL service
3. **Root Password**: Configureert een root wachtwoord voor MySQL
4. **Database Aanmaken**: Creëert een applicatie database (`myapp_db`)
5. **Database User**: Maakt een dedicated database gebruiker aan (`webapp`)