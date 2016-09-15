#!/bin/bash
//bin/true && SCRIPT_DIR="$(dirname $(readlink -f "${0}"))"
//bin/true && exec groovy -cp "${SCRIPT_DIR}/lib" "${0}" "${@}"; exit $?
import it.italiaonline.rnd.filters.TextFilter;

for ( String test : args ) {
  new TextFilter.SmartCap(test).result()
}

