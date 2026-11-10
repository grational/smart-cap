package it.italiaonline.rnd.filters;

import java.util.regex.Pattern;

public class CommaSpacerFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile(",(?=[^ \\t])");
	private final TextFilter origin;

	public CommaSpacerFilter(TextFilter origin) {
		this.origin = origin;
	}

	@Override
	public String result() {
		return PATTERN.matcher(origin.result()).replaceAll(", ");
	}
}
