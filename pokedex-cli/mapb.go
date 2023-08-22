package main

import (
	"errors"
	"fmt"
)

func commandMapB(cfg *config) error {

	if cfg.prevLocationAreaURL == nil {
		return errors.New("you are on the first page")
	}

	res, err := cfg.pokeapiClient.ListLocationAreas(cfg.prevLocationAreaURL)

	if err != nil {
		return err
	}

	for _, area := range res.Results {
		fmt.Printf(" - %s\n", area.Name)
	}

	cfg.nextLocationAreaURL = res.Next
	cfg.prevLocationAreaURL = res.Previous

	return nil
}
