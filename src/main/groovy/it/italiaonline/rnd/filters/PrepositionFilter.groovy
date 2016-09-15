package it.italiaonline.rnd.filters

import java.util.regex.Pattern

class PrepositionFilter implements TextFilter {

  private final TextFilter origin
  private final Pattern pattern =
    ~/(?i)(?<=\h)(?:sullo|sulle|sulla|sugli|nello|nelle|nella|negli|dello|delle|della|degli|dallo|dalle|dalla|dagli|allo|alle|alla|agli|tra|sul|sui|per|nel|nei|fra|del|dei|dal|dai|con|su|in|di|da|al|ai|ad|a)(?=\h)/

  PrepositionFilter(TextFilter orig) {
    this.origin = orig
  }

  @Override
  String result() {
    origin.result().replaceAll(pattern) {
      it.toLowerCase()
    }
  }
}
