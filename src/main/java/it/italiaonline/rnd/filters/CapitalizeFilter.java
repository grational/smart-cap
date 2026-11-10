package it.italiaonline.rnd.filters;

import java.util.regex.Pattern;

public class CapitalizeFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile("(?<=\\b|_)[a-z]");
	private final TextFilter origin;

	public CapitalizeFilter(TextFilter origin) {
		this.origin = origin;
	}

	@Override
	public String result() {
		return RegexReplacement.replaceAll(origin.result().toLowerCase(), PATTERN,
			match -> match.group().toUpperCase());
	}
}
