#!/bin/sh -e
set -x

for db in `psql -c '\l' | grep harmony_auth_test* | cut -d '|' -f 1`; do psql -c "drop database \"$db\" "; done
for db in `psql -c '\l' | grep harmony_channel_test* | cut -d '|' -f 1`; do psql -c "drop database \"$db\" "; done
for db in `psql -c '\l' | grep harmony_portal_test* | cut -d '|' -f 1`; do psql -c "drop database \"$db\" "; done
