package it.italiaonline.rnd.filters;

import java.util.regex.Pattern;

public class SimpleConjunctionFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile("(?i)(?<=[ \\t])(?:ed|e|o)(?=[ \\t])");
	private final TextFilter origin;

	public SimpleConjunctionFilter(TextFilter origin) {
		this.origin = origin;
	}

	@Override
	public String result() {
		return RegexReplacement.replaceAll(origin.result(), PATTERN,
			match -> match.group().toLowerCase());
	}
}
