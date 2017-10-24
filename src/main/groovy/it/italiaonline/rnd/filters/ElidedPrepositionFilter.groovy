package it.italiaonline.rnd.filters

import java.util.regex.Pattern

class ElidedPrepositionFilter implements TextFilter {

  private final TextFilter origin
  private final Pattern pattern = ~/(?i)(?<=[ \t])(?:sull|nell|dell|dall|all)(?='[a-z])/

  ElidedPrepositionFilter(TextFilter orig) {
    this.origin = orig
  }

  @Override
  String result() {
    origin.result().replaceAll(pattern) {
      it.toLowerCase()
    }
  }
}
