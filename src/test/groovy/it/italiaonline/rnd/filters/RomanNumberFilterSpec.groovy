package it.italiaonline.rnd.filters

import spock.lang.Specification

class RomanNumberFilterSpec extends Specification {

	def "Should make roman numbers digits all in uppercase"() {

		expect:
			output == new RomanNumberFilter(
			            new TextFilter.NoNullFilter(input)
			          ).result()

		where:
			input                                                 | output
			"di questo xx"                                        | "di questo XX"
			"a noi vii focacce"                                   | "a noi VII focacce"
			"venuti da cupertino xii"                             | "venuti da cupertino XII"
			"in sella alla motoslitta l"                          | "in sella alla motoslitta L"
			"i,ii,iii,iv,v,vi,vii,viii,ix,x"                      | "I,II,III,IV,V,vi,VII,VIII,IX,X"
			"xi,xii,xiii,xiv,xv,xvi,xvii,xviii,xix,xx"            | "XI,XII,XIII,XIV,XV,XVI,XVII,XVIII,XIX,XX"
			"xxi,xxii,xxiii,xxiv,xxv,xxvi,xxvii,xxviii,xxix,xxx"  | "XXI,XXII,XXIII,XXIV,XXV,XXVI,XXVII,XXVIII,XXIX,XXX"
			"... xl,"                                             | "... XL,"
			"xli,xlii,xliii,xliv,xlv,xlvi,xlvii,xlviii,xlix,l"    | "XLI,XLII,XLIII,XLIV,XLV,XLVI,XLVII,XLVIII,XLIX,L"
			"xc,xci,xcii,xciii,xciv,xcv,xcvi,xcvii,xcviii,xcix,c" | "XC,XCI,XCII,XCIII,XCIV,XCV,XCVI,XCVII,XCVIII,XCIX,C"
			"ci,cii"                                              | "ci,CII"
			"mi,di,ci,li,vi"                                      | "mi,di,ci,li,vi"
	}
}
