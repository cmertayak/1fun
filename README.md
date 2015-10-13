## PostgreSQL backed

Installation is done with brew. The package name is postgresql.

In order to make postgres start at the launch:
```bash
ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
```

Or in order to run it directly:
```bash
postgres -D /usr/local/var/postgres/
```

In order to connect to the database:
```bash
psql mydb --username=dev
```

## Migration Specific Manage Commands

1. makemigrations
1. sqlmigrate
1. squashmigrations
1. migrate

## Githooks
Symlink .git/hooks to scripts/githooks/

```bash
ln -s scripts/githooks/ .git/hooks
```
