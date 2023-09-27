package it.italiaonline.rnd.filters

import org.apache.commons.text.similarity.JaroWinklerDistance

/**
 * This interface defines an object capable of declaring its support status for
 * the http2 and spdy protocols (usually a webserver).
 */
interface TextFilter {
	String result()

	final class NoNullFilter implements TextFilter {
		private final String input

		NoNullFilter(String inpt) {
			this.input = inpt
		}

		@Override
		String result() throws IllegalArgumentException {
			if (input == null) {
				throw new IllegalArgumentException("Input is NULL: can't go ahead.")
			}
			this.input
		}
	}

	/**
	 * Smart class to compact the vertical decorators
	 */
	final class SmartCap implements TextFilter {

		private final String input

		SmartCap(String inpt) {
			this.input = inpt
		}
		@Override
		String result() {
			new ProvinceAbbreviationFilter (
				new ElidedPrepositionFilter (
					new PrepositionFilter (
						new AbbreviationFilter (
							new URLFilter (
								new SimpleConjunctionFilter (
									new CompanyTypeAcronymFilter (
										new RomanNumberFilter (
											new CapitalizeFilter (
												new NoNullFilter (
													this.input
												)
											)
										)
									)
								)
							)
						)
					)
				)
			).result()
		}
	}

	/**
	 * Smart class with some customizations for address
	 */
	final class AddressSmartCap implements TextFilter {

		private final String input

		AddressSmartCap(String inpt) {
			this.input = inpt
		}

		@Override
		String result() {
			new CommaSpacerFilter(
				new TownApostrophe2AccentFilter(
					new TextFilter.SmartCap(this.input)
				)
			).result()
		}
	}

	/**
	 * Smart class that apply the filters just if the original
	 * string have a string distance above a certain threshold
	 */
	final class ConditionalSmartCap implements TextFilter {

		private final String input
		private final Double threshold

		ConditionalSmartCap(
			String inpt,
			Double  thr
		) {
			this.input     = inpt
			this.threshold = thr
		}

		@Override
		String result() {
			def result
			def filtered = new TextFilter.SmartCap(this.input).result()
			def distance = new JaroWinklerDistance().apply(
				filtered,
				this.input
			)
			if ( distance >= this.threshold )
				result = this.input
			else
				result = filtered
			
			return result
		}
	}

}
