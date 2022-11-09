public class RabinKarp {
	
	public final static int d = 256;

	static void search(String pat, String txt, int q)
	{
		int M = pat.length();
		int N = txt.length();
		int i, j;
		int p = 0; 
		int t = 0; 
		int h = 1;

		
		for (i = 0; i < M - 1; i++)
			h = (h * d) % q;

		
		for (i = 0; i < M; i++) {
			p = (d * p + pat.charAt(i)) % q;
			t = (d * t + txt.charAt(i)) % q;
		}

		
		for (i = 0; i <= N - M; i++) {

			
			if (p == t) {
				
				for (j = 0; j < M; j++) {
					if (txt.charAt(i + j) != pat.charAt(j))
						break;
				}

			
				if (j == M)
					System.out.println(
						"Pattern found at index " + i);
			}

			// Calculate hash value for next window of text:
			// Remove leading digit, add trailing digit
			if (i < N - M) {
				t = (d * (t - txt.charAt(i) * h)
					+ txt.charAt(i + M))
					% q;

				// We might get negative value of t,
				// converting it to positive
				if (t < 0)
					t = (t + q);
			}
		}
	}

	/* Driver Code */
	public static void main(String[] args)
	{
		String txt = "GEEKS FOR GEEKS";
		String pat = "GEEK";

		// A prime number
		int q = 101;

		// Function Call
		search(pat, txt, q);
	}
}