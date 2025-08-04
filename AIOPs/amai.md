# amai


## n8n 

1. podman volume create n8n_data
2. podman run -it --rm --name n8n -p 5678:5678 -e N8N_SECURE_COOKIE="false" -e TZ="Asia/Kolkata" -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
3. export N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true


## postgresql

1. sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-$(rpm -E %{rhel})-x86_64/pgdg-redhat-repo-latest.noarch.rpm
2. sudo dnf -qy module disable postgresql
4. sudo dnf install pgvector_17
6. sudo /usr/pgsql-17/bin/postgresql-17-setup initdb
11. sudo systemctl start postgresql-17
12. sudo systemctl enable postgresql-17
13. sudo -i -u postgres
15. psql
16. CREATE ROLE amai_user WITH LOGIN PASSWORD 'a_strong_password';
17. CREATE DATABASE amai_knowledge_db OWNER amai_user;
18. \c amai_knowledge_db
19. CREATE EXTENSION IF NOT EXISTS vector;
20. \dx vector
21. \q
22. exit
23. sudo nano /var/lib/pgsql/17/data/postgresql.conf
24. listen_addresses = '*'
25. sudo nano /var/lib/pgsql/17/data/pg_hba.conf
26. host    amai_knowledge_db   amai_user   0.0.0.0/0               scram-sha-256
27. sudo systemctl restart postgresql-17
28. sudo firewall-cmd --permanent --add-port=5432/tcp
29. sudo firewall-cmd --reload
```bash
DB_HOST: 192.168.2.226
DB_PORT: 5432
DB_NAME: amai_knowledge_db
DB_USER: amai_user
DB_PASSWORD: 'a_strong_password'
``` 
