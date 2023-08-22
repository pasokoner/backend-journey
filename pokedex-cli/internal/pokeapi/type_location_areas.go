package pokeapi

type LocationAreasResponse struct {
	Count    int     `json:"count"`
	Next     *string `json:"next"`     // Use a pointer to represent nullable string
	Previous *string `json:"previous"` // Use a pointer to represent nullable string
	Results  []struct {
		Name string `json:"name"`
		URL  string `json:"url"`
	} `json:"results"`
}
