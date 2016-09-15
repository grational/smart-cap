package it.italiaonline.rnd.filters

import spock.lang.Specification

class PrepositionFilterSpec extends Specification {

  def "Should make prepositions in lowercase"() {

    expect:
      output == new PrepositionFilter(
                  new TextFilter.NoNullFilter(input)
                ).result()

    where:
      input                           | output
      "PERCIÒ DI QUESTO"              | "PERCIÒ di QUESTO"
      "A NOI, PROPRIO A NOI"          | "A NOI, PROPRIO a NOI"
      "VENUTI DA CUPERTINO"           | "VENUTI da CUPERTINO"
      "IN SELLA ALLA MOTOSLITTA"      | "IN SELLA alla MOTOSLITTA"
      "PURE CON TANTA CAPARBIETÀ"     | "PURE con TANTA CAPARBIETÀ"
      "FIN SU PER LA MONTAGNA"        | "FIN su per LA MONTAGNA"
      "SALENDO TRA FIERI STAMBECCHI"  | "SALENDO tra FIERI STAMBECCHI"
      "E FRA CESPUGLI ODOROSI"        | "E fra CESPUGLI ODOROSI"
      "NON INTERESSA."                | "NON INTERESSA."
      "ODE AD OGNI PIE' SOSPESO"      | "ODE ad OGNI PIE' SOSPESO"
      "E AL SOSPIRO DEL VENTO"        | "E al SOSPIRO del VENTO"
      "E ALLO SCALPICCIO DEI CAVALLI" | "E allo SCALPICCIO dei CAVALLI"

  }
  //DI   V
  //A    V
  //DA   V
  //IN   V
  //CON  V
  //SU   V
  //PER  V
  //TRA  V
  //FRA  V
  /* COMPOSTE */
  //AD      V
  //AL      V
  //ALLO    X
  //ALL'    X
  //ALLA    X
  //AI      X
  //AGLI    X
  //ALLE    X
  //DA      X
  //DAL     X
  //DALLO   X
  //DALL'   X
  //DALLA ? X
  //DAI     X
  //DAGLI   X
  //DALLE   X
  //DI      X
  //DEL     V
  //DELLO   X
  //DELL'   X
  //DELLA   X
  //DEI     V
  //DEGLI   X
  //DELLE   X
  //IN      X
  //NEL     X
  //NELLO   X
  //NELL'   X
  //NELLA ? X
  //NEI   ? X
  //NEGLI   X
  //NELLE   X
  //SUL     X
  //SULLO   X
  //SULL'   X
  //SULLA   X
  //SUI     X
  //SUGLI   X
  //SULLE   X
}
