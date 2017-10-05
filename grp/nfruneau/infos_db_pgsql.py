# pgsql:

# installation:
# brew install postgresql
# emacs ~/.zshrc
# #POSTGRESQL
# export PGDATA=$HOME/.brew/var/postgres
# emacs ~/.brew/var/postgres/pg_hba.conf
# ligne #IPv4 local connections modifier METHOD trust en md5

# pg_ctlstart
# psql -d postgres
# ou
# psql -U <username> -d <namedtb>

# commandes:
# \? <- liste des commandes
# \l <- liste des databases
# \d <- liste de relations entre tables
# CREATE DATABASE <namedtb>;
# CREATE USER <username> WITH PASSWORD <pass>
# ALTER DATABASE <namedtb> OWNER TO <username>

# psycogpg2:
# pip3 install psycopg2
