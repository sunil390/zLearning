# amai

## postgresql

1. sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-$(rpm -E %{rhel})-x86_64/pgdg-redhat-repo-latest.noarch.rpm
2. sudo dnf -qy module disable postgresql
3. sudo dnf install -y postgresql15-server postgresql15-contrib
4. sudo /usr/pgsql-15/bin/postgresql-15-setup initdb
5. sudo systemctl start postgresql-15
6. sudo systemctl enable postgresql-15
7. sudo -i -u postgres
8. psql
9. CREATE ROLE amai_user WITH LOGIN PASSWORD 'a_strong_password';
10. CREATE DATABASE amai_knowledge_db OWNER amai_user;
11. \c amai_knowledge_db
12. CREATE EXTENSION IF NOT EXISTS vector;
13. \dx vector
14. \q
15. exit
16. sudo nano /var/lib/pgsql/15/data/postgresql.conf
17. listen_addresses = '*'
18. sudo nano /var/lib/pgsql/15/data/pg_hba.conf
19. host    amai_knowledge_db   amai_user   0.0.0.0/0               scram-sha-256
20. sudo systemctl restart postgresql-15
21. sudo firewall-cmd --permanent --add-port=5432/tcp
22. sudo firewall-cmd --reload
```bash
DB_HOST: 192.168.2.226
DB_PORT: 5432
DB_NAME: amai_knowledge_db
DB_USER: amai_user
DB_PASSWORD: 'a_strong_password'
```

24. 
