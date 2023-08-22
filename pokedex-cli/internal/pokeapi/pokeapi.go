package pokeapi

import (
	"net/http"
	"time"
)

const baseURL = "https://pokeapi.co/api/v2"

type Client struct {
	httpClient http.Client
}

func NewClient() Client {
	return Client{
		httpClient: http.Client{
			Timeout: time.Minute,
		},
	}
}

// res, err := http.Get("https://pokeapi.co/api/v2/location")
// if err != nil {
// 	log.Fatal(err)
// }
// body, err := io.ReadAll(res.Body)
// res.Body.Close()
// if res.StatusCode > 299 {
// 	log.Fatalf("Response failed with status code: %d and\nbody: %s\n", res.StatusCode, body)
// }
// if err != nil {
// 	log.Fatal(err)
// }
// locations := Locations{}
// errParse := json.Unmarshal(body, &locations)
// if errParse != nil {
// 	fmt.Println(err)
// }
// fmt.Println(*locations.Previous)
