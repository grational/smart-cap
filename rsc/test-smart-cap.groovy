#!/bin/bash
//bin/true && SCRIPT_DIR="$(dirname $(readlink -f "${0}"))"
//bin/true && exec groovy -cp "${SCRIPT_DIR}/lib" "${0}" "${@}"; exit $?
import it.italiaonline.rnd.filters.TextFilter

def GScript = this.class.name

if ( ! args ) {
  println "Usage: ${GScript} <businessName>"
  System.exit 1
}

println new TextFilter.SmartCap(args[0]).result()
