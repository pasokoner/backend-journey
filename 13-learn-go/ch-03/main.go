package main

import (
	"fmt"
)

func yearsUntilEvents(age int) (yearsUntilAdult int, yearsUntilCarRental int, yearsUntilDrinking int) {

	yearsUntilAdult = 18 - age
	if yearsUntilAdult < 0 {
		yearsUntilAdult = 0
	}
	yearsUntilDrinking = 21 - age
	if yearsUntilDrinking < 0 {
		yearsUntilDrinking = 0
	}
	yearsUntilCarRental = 25 - age
	if yearsUntilCarRental < 0 {
		yearsUntilCarRental = 0
	}
	return
}

// don't edit below this line

func test(age int) {
	fmt.Println("Age:", age)
	yearsUntilAdult, yearsUntilDrinking, yearsUntilCarRental := yearsUntilEvents(age)
	fmt.Println("You are an adult in", yearsUntilAdult, "years")
	fmt.Println("You can drink in", yearsUntilDrinking, "years")
	fmt.Println("You can rent a car in", yearsUntilCarRental, "years")
	fmt.Println("====================================")
}

func main() {
	test(4)
	test(10)
	test(22)
	test(35)
}

// // 07
// package main

// import "fmt"

// func main() {
// 	firstName, _ := getNames()
// 	fmt.Println("Welcome to Textio,", firstName)
// }

// // don't edit below this line

// func getNames() (string, string) {
// 	return "John", "Doe"
// }

// // 06
// package main

// import "fmt"

// func main() {
// 	sendsSoFar := 430
// 	const sendsToAdd = 25
// 	sendsSoFar = incrementSends(sendsSoFar, sendsToAdd)
// 	fmt.Println("you've sent", sendsSoFar, "messages")
// }

// func incrementSends(sendsSoFar, sendsToAdd int) int {
// 	sendsSoFar = sendsSoFar + sendsToAdd

// 	return sendsSoFar
// }

// // 01
// package main

// import "fmt"

// func concat(s1 string, s2 string) string {
// 	return s1 + s2
// }

// // don't touch below this line

// func main() {
// 	test("Lane,", " happy birthday!")
// 	test("Elon,", " hope that Tesla thing works out")
// 	test("Go", " is fantastic")
// }

// func test(s1 string, s2 string) {
// 	fmt.Println(concat(s1, s2))
// }
