# Book Scraper
Link: https://octopus-app-3-6xu4s.ondigitalocean.app

## Endpoint
1. /geturl
This endpoint recieves Book keywords an returns book Titles and their corresponding download links.

Request Body:
```
{
	"keywords":"My Book of Bible Stories"
}
```
Request Headers:
```
{
"content-Type":"application/json"
}
```

### Example Response
```
Response:200, OK
{
"titles":[
          "Bible Story1",
          "Bible Story2"
         ],
"links":[
         "https://librarylol.com/sdijfsodj",
         "https://librarylol..com/sodijjfiosdihf"
        ],
"images":[
           "https://librarylol.com/sddfdj",
           "https://librarylol..com/sodijf"
         ]
}
```

### Javascript

```
async function fetchBooks(bookCode: string) {
  let endpoints = []
  let images = []
  let titles = []
  try {
    const response = await fetch('https://octopus-app-3-6xu4s.ondigitalocean.app/geturl', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ keywords: bookCode })
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error.message)
  }
}

export {fetchBooks}
```

### Python

```
import asyncio
import json
import aiohttp

async def fetch_books(book_code: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                'https://octopus-app-3-6xu4s.ondigitalocean.app/geturl',
                headers={'Content-Type': 'application/json'},
                data=json.dumps({'keywords': book_code})
            ) as response:
                data = await response.json()
                return data
    except aiohttp.ClientError as e:
        print(e)

# Example usage:
async def main():
    book_code = "your_book_code_here"
    result = await fetch_books(book_code)
    print(result)

asyncio.run(main())

```

### Java

```
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.logging.Level;
import java.util.logging.Logger;

public class BookFetcher {
    private static final Logger LOGGER = Logger.getLogger(BookFetcher.class.getName());

    public static void fetchBooks(String bookCode) {
        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                   .uri(URI.create("https://octopus-app-3-6xu4s.ondigitalocean.app/geturl"))
                   .header("Content-Type", "application/json")
                   .POST(HttpRequest.BodyPublishers.ofString("{\"keywords\":\"" + bookCode + "\"}"))
                   .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println(response.body());
        } catch (IOException | InterruptedException e) {
            LOGGER.log(Level.SEVERE, "Error fetching books", e);
        }
    }

    public static void main(String[] args) {
        fetchBooks("your_book_code_here");
    }
}
```

### Rust

```
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.logging.Level;
import java.util.logging.Logger;

public class BookFetcher {
    private static final Logger LOGGER = Logger.getLogger(BookFetcher.class.getName());

    public static void fetchBooks(String bookCode) {
        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                   .uri(URI.create("https://octopus-app-3-6xu4s.ondigitalocean.app/geturl"))
                   .header("Content-Type", "application/json")
                   .POST(HttpRequest.BodyPublishers.ofString("{\"keywords\":\"" + bookCode + "\"}"))
                   .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println(response.body());
        } catch (IOException | InterruptedException e) {
            LOGGER.log(Level.SEVERE, "Error fetching books", e);
        }
    }

    public static void main(String[] args) {
        fetchBooks("your_book_code_here");
    }
}
```

### PHP

```
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.logging.Level;
import java.util.logging.Logger;

public class BookFetcher {
    private static final Logger LOGGER = Logger.getLogger(BookFetcher.class.getName());

    public static void fetchBooks(String bookCode) {
        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                   .uri(URI.create("https://octopus-app-3-6xu4s.ondigitalocean.app/geturl"))
                   .header("Content-Type", "application/json")
                   .POST(HttpRequest.BodyPublishers.ofString("{\"keywords\":\"" + bookCode + "\"}"))
                   .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println(response.body());
        } catch (IOException | InterruptedException e) {
            LOGGER.log(Level.SEVERE, "Error fetching books", e);
        }
    }

    public static void main(String[] args) {
        fetchBooks("your_book_code_here");
    }
}
