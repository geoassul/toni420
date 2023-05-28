
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;


public class scrapping1 {

	public static void main(String[] args) throws IOException {
		
		// Make a URL to the web page
		URL url = new URL("http://stackoverflow.com/questions/6159118/using-java-to-pull-data-from-a-webpage");
		
		// Get the input stream through URL Connection
		URLConnection con = url.openConnection();
		InputStream is = con.getInputStream();
		
		// Once you have the Input Stream, it's just plain old Java IO stuff.
		
		// For this case, since you are interested in getting plain-text web page
		// I'll use a reader and output the text content to System.out.
		
		// For binary content, it's better to directly read the bytes from stream and write
		// to the target file.          
		
		try(BufferedReader br = new BufferedReader(new InputStreamReader(is))) {
			String line = null;
		
			// read each line and write to System.out
			while ((line = br.readLine()) != null) {
				System.out.println(line);
			}
		}
	}
}
