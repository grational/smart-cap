package it.italiaonline.rnd.filters

import java.util.regex.Pattern

class CommaSpacerFilter implements TextFilter {

  private final TextFilter origin
  private final Pattern pattern = ~/,(?=\H)/

  CommaSpacerFilter(TextFilter orig) {
    this.origin = orig
  }

  @Override
  String result() {
    origin.result().replaceAll(pattern,', ')
  }
}
