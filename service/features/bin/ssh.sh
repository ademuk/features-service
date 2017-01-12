#!/bin/sh

if [ -z "$PKEY" ]; then
    ssh "$@"
else
    ssh -i "$PKEY" -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "$@"
fi