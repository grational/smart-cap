package it.italiaonline.rnd.filters;

import java.util.regex.Pattern;

public class PrepositionFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile("(?i)(?<=[ \\t])(?:sullo|sulle|sulla|sugli|nello|nelle|nella|negli|dello|delle|della|degli|dallo|dalle|dalla|dagli|allo|alle|alla|agli|tra|sul|sui|per|nel|nei|fra|del|dei|dal|dai|con|su|in|di|da|al|ai|ad|a)(?=[ \\t])");
	private final TextFilter origin;

	public PrepositionFilter(TextFilter origin) {
		this.origin = origin;
	}

	@Override
	public String result() {
		return RegexReplacement.replaceAll(origin.result(), PATTERN,
			match -> match.group().toLowerCase());
	}
}
