package it.italiaonline.rnd.filters;

import org.apache.commons.text.similarity.JaroWinklerSimilarity;

/** A text transformation whose output is available through {@link #result()}. */
@FunctionalInterface
public interface TextFilter {
	String result();

	final class NoNullFilter implements TextFilter {
		private final String input;

		public NoNullFilter(String input) {
			this.input = input;
		}

		@Override
		public String result() {
			if (input == null) {
				throw new IllegalArgumentException("Input is NULL: can't go ahead.");
			}
			return input;
		}
	}

	/** Capitalizes Italian business names while preserving recognized abbreviations. */
	final class SmartCap implements TextFilter {
		private final String input;

		public SmartCap(String input) {
			this.input = input;
		}

		@Override
		public String result() {
			TextFilter filter = new NoNullFilter(input);
			filter = new CapitalizeFilter(filter);
			filter = new RomanNumberFilter(filter);
			filter = new CompanyTypeAcronymFilter(filter);
			filter = new SimpleConjunctionFilter(filter);
			filter = new URLFilter(filter);
			filter = new AbbreviationFilter(filter);
			filter = new PrepositionFilter(filter);
			filter = new ElidedPrepositionFilter(filter);
			return new ProvinceAbbreviationFilter(filter).result();
		}
	}

	/** Also normalizes comma spacing and known town accents. */
	final class AddressSmartCap implements TextFilter {
		private final String input;

		public AddressSmartCap(String input) {
			this.input = input;
		}

		@Override
		public String result() {
			return new CommaSpacerFilter(new TownApostrophe2AccentFilter(new SmartCap(input))).result();
		}
	}

	/** Preserves the original text when its similarity reaches the threshold. */
	final class ConditionalSmartCap implements TextFilter {
		private final String input;
		private final Double threshold;

		public ConditionalSmartCap(String input, Double threshold) {
			this.input = input;
			this.threshold = threshold;
		}

		@Override
		public String result() {
			String filtered = new SmartCap(input).result();
			double similarity = new JaroWinklerSimilarity().apply(filtered, input);
			// Groovy's comparison with a null threshold historically preserved the input.
			return threshold == null || similarity >= threshold ? input : filtered;
		}
	}
}
