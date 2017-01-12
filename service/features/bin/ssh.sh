#!/bin/sh

ssh -i "$PRIVATE_KEY" -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "$@"
