package it.italiaonline.rnd.filters

import java.util.regex.Pattern

class CutPrepositionFilter implements TextFilter {

  private final TextFilter origin
  private final Pattern pattern = ~/(?i)(?<=\h)(?:sull|nell|dell|dall|all)(?='[a-z])/

  CutPrepositionFilter(TextFilter orig) {
    this.origin = orig
  }

  @Override
  String result() {
    origin.result().replaceAll(pattern) {
      it.toLowerCase()
    }
  }
}
