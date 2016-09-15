package it.italiaonline.rnd.filters

import spock.lang.Specification

class CapitalizeFilterSpec extends Specification {

  def "Should lowercase every words and Capitalize the first letter"() {

    expect:
      output == new CapitalizeFilter(
                  new TextFilter.NoNullFilter(input)
                ).result()

    where:
      input                         | output
      "DI QUESTO"                   | "Di Questo"
      "A NOI"                       | "A Noi"
      "VENUTI DA CUPERTINO"         | "Venuti Da Cupertino"
      "IN SELLA ALLA MOTOSLITTA"    | "In Sella Alla Motoslitta"
      "CON TANTA CAPARBIETÀ"        | "Con Tanta Caparbietà"
      "SU PER LA MONTAGNA"          | "Su Per La Montagna"
      "TRA FIERI STAMBECCHI"        | "Tra Fieri Stambecchi"
      "FRA CESPUGLI ODOROSI"        | "Fra Cespugli Odorosi"
      "NON INTERESSA"               | "Non Interessa"
      "AD OGNI PIE' SOSPESO"        | "Ad Ogni Pie' Sospeso"
      "AL SOSPIRO DEL VENTO"        | "Al Sospiro Del Vento"
      "ALLO SCALPICCIO DEI CAVALLI" | "Allo Scalpiccio Dei Cavalli"
      "TE-ST"                       | "Te-St"

  }

}
