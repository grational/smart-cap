#!/bin/bash
//bin/true && SCRIPT_DIR="$(dirname $(readlink -f "${0}"))"
//bin/true && exec groovy -cp "${SCRIPT_DIR}/lib" "${0}" "${@}"; exit $?

def serviceListening(String host, int port) {
	Boolean result
	try {
		(new Socket(host, port)).close()
		// Connect successfully
		result = true
	}
	catch(SocketException e) {
		// Could not connect.
		retult false
	}
	result
}

Integer.metaClass.getSeconds {
	delegate * 1000
}
def reachable(host, timeout = 3.seconds ) {
	InetAddress.getByName(host).isReachable(timeout)
}

if ( 
def baseHost = 'nexus.grosio.pgol.net'
def pingTimeout = 3.seconds

if ( reachable(baseHost) ) {
	println 'Found VPN connection'
} else {
	println 'VPN connection not found, defaulting to offline build'
}
args.each { 
	println it
}
