package main

import "fmt"

func commandHelp() error {

	commands := getCommands()
	fmt.Println("=====DISPLAYING COMMANDS=====")
	for c, item := range commands {
		fmt.Printf("%v - %v\n", c, item.description)
	}

	return nil
}
