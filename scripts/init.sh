#!/bin/sh

PATH="/usr/local/bin:$PATH"
DEFAULT_CONF_FILE=scripts/conf/init.default.conf
CUSTOM_CONF_FILE=scripts/conf/init.conf

source ${DEFAULT_CONF_FILE}
[[ -f ${CUSTOM_CONF_FILE} ]] && source ${CUSTOM_CONF_FILE} || \
    echo "$CUSTOM_CONF_FILE not found, using $DEFAULT_CONF_FILE"
source ${VIRTUAL_ENV_PATH}/bin/activate

export PIP_REQUIRE_VIRTUALENV=true
