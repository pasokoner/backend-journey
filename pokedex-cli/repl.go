package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func cleanInput(i string) []string {
	lowered := strings.ToLower(i)
	words := strings.Fields(lowered)

	return words
}

func startRepl() {
	scanner := bufio.NewScanner(os.Stdin)
	commands := getCommands()

	for {
		fmt.Print("Pokedex > ")

		scanner.Scan()
		userInput := scanner.Text()

		words := cleanInput(userInput)

		if len(words) == 0 {
			continue
		}

		c, ok := commands[words[0]]

		if !ok {
			fmt.Println("invalid commands")

			continue
		}

		err := c.callback()

		if err != nil {
			fmt.Println(err)
		}

	}

}
