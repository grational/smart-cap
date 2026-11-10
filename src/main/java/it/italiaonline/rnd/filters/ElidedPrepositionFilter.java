package it.italiaonline.rnd.filters;

import java.util.regex.Pattern;

public class ElidedPrepositionFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile("(?i)(?<=[ \\t])(?:sull|nell|dell|dall|all)(?='[a-z])");
	private final TextFilter origin;

	public ElidedPrepositionFilter(TextFilter origin) {
		this.origin = origin;
	}

	@Override
	public String result() {
		return RegexReplacement.replaceAll(origin.result(), PATTERN,
			match -> match.group().toLowerCase());
	}
}
