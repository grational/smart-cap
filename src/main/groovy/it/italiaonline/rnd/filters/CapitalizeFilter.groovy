package it.italiaonline.rnd.filters

import java.util.regex.Pattern

class CapitalizeFilter implements TextFilter {

  private final TextFilter origin
  //private final Pattern pattern = ~/(?<=^|[^\w\p{Pd}])[a-z]/
  private final Pattern pattern = ~/(?<=\b|_)[a-z]/

  CapitalizeFilter(TextFilter orig) {
    this.origin = orig
  }

  @Override
  String result() {
    origin.result().toLowerCase().replaceAll(pattern) {
      it.toUpperCase()
    }
  }
}
