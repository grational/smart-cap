package it.italiaonline.rnd.filters

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
			new CutPrepositionFilter(
			  new PrepositionFilter(
			    new AbbreviationFilter(
			      new SimpleConjunctionFilter(
			        new CompanyTypeAcronymFilter(
			          new RomanNumberFilter(
			            new CapitalizeFilter(
			              new NoNullFilter(
			                this.input
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
				new TextFilter.SmartCap(this.input)
			).result()
		}
	}

}
