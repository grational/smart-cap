package it.italiaonline.rnd.filters

import spock.lang.*

class URLFilterSpec extends Specification {

	@Unroll
	def "Should render URL authority in lowercase and the rest has to be maintained"() {

		expect:
			output == new URLFilter (
				new TextFilter.NoNullFilter(input)
			).result()

		where:
			input                                   || output
			"HTTP://WWW.PREZZOFORTE.IT/aBoUt.hTmL"  || "http://www.prezzoforte.it/about.html"
			"FTP://WWW.PREZZOFORTE.IT/aBoUt.hTmL"   || "ftp://www.prezzoforte.it/about.html"
			"HTTPS://WWW.PREZZOFORTE.IT/aBoUt.hTmL" || "https://www.prezzoforte.it/about.html"
			"FTPS://WWW.PREZZOFORTE.IT/aBoUt.hTmL"  || "ftps://www.prezzoforte.it/about.html"
			"ICOMMERCE SRL (www.prezzoforte.it)"    || "ICOMMERCE SRL (www.prezzoforte.it)"
  }

}
