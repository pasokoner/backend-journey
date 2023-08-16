// 16
package main

import (
	"fmt"
	"slices"
)

func indexOfFirstBadWord(msg []string, badWords []string) int {
	for i, m := range msg {
		if slices.Contains(badWords, m) {
			return i
		}
	}

	return -1
}

// don't touch below this line

func test(msg []string, badWords []string) {
	i := indexOfFirstBadWord(msg, badWords)
	fmt.Printf("Scanning message: %v for bad words:\n", msg)
	for _, badWord := range badWords {
		fmt.Println(` -`, badWord)
	}
	fmt.Printf("Index: %v\n", i)
	fmt.Println("====================================")
}

func main() {
	badWords := []string{"crap", "shoot", "dang", "frick"}
	message := []string{"hey", "there", "john"}
	test(message, badWords)

	message = []string{"ugh", "oh", "my", "frick"}
	test(message, badWords)

	message = []string{"what", "the", "shoot", "I", "hate", "that", "crap"}
	test(message, badWords)
}

// //12
// package main

// import "fmt"

// func createMatrix(rows, cols int) [][]int {
// 	matrix := [][]int{}

// 	for i := 0; i < rows; i++ {
// 		matrix = append(matrix, []int{})
// 		for j := 0; j < cols; j++ {
// 			value := j * i

// 			matrix[i] = append(matrix[i], value)
// 		}
// 	}

// 	return matrix
// }

// // dont edit below this line

// func test(rows, cols int) {
// 	fmt.Printf("Creating %v x %v matrix...\n", rows, cols)
// 	matrix := createMatrix(rows, cols)
// 	for i := 0; i < len(matrix); i++ {
// 		fmt.Println(matrix[i])
// 	}
// 	fmt.Println("===== END REPORT =====")
// }

// func main() {
// 	test(3, 3)
// 	test(5, 5)
// 	test(10, 10)
// 	test(15, 15)
// }

// 11
// package main

// import "fmt"

// type cost struct {
// 	day   int
// 	value float64
// }

// func getCostsByDay(costs []cost) []float64 {
// 	lastDay := costs[len(costs)-1].day + 1
// 	dayCosts := make([]float64, lastDay)

// 	for i := 0; i < len(costs); i++ {
// 		dayCosts[costs[i].day] += costs[i].value
// 	}

// 	return dayCosts
// }

// // dont edit below this line

// func test(costs []cost) {
// 	fmt.Printf("Creating daily buckets for %v costs...\n", len(costs))
// 	costsByDay := getCostsByDay(costs)
// 	fmt.Println("Costs by day:")
// 	for i := 0; i < len(costsByDay); i++ {
// 		fmt.Printf(" - Day %v: %.2f\n", i, costsByDay[i])
// 	}
// 	fmt.Println("===== END REPORT =====")
// }

// func main() {
// 	test([]cost{
// 		{0, 1.0},
// 		{1, 2.0},
// 		{1, 3.1},
// 		{2, 2.5},
// 		{3, 3.6},
// 		{3, 2.7},
// 		{4, 3.34},
// 	})
// 	test([]cost{
// 		{0, 1.0},
// 		{10, 2.0},
// 		{3, 3.1},
// 		{2, 2.5},
// 		{1, 3.6},
// 		{2, 2.7},
// 		{4, 56.34},
// 		{13, 2.34},
// 		{28, 1.34},
// 		{25, 2.34},
// 		{30, 4.34},
// 	})
// }

// // 10
// package main

// import "fmt"

// func sum(nums ...float64) float64 {
// 	total := 0.0

// 	for i := 0; i < len(nums); i++ {
// 		total += nums[i]
// 	}

// 	return total
// }

// // don't edit below this line

// func test(nums ...float64) {
// 	total := sum(nums...)
// 	fmt.Printf("Summing %v costs...\n", len(nums))
// 	fmt.Printf("Bill for the month: %.2f\n", total)
// 	fmt.Println("===== END REPORT =====")
// }

// func main() {
// 	test(1.0, 2.0, 3.0)
// 	test(1.0, 2.0, 3.0, 4.0, 5.0)
// 	test(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0)
// 	test(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0)
// }

// // 06
// package main

// import "fmt"

// func getMessageCosts(messages []string) []float64 {
// 	messageCost := make([]float64, len(messages))

// 	for i := 0; i < len(messages); i++ {
// 		messageCost[i] = float64(len(messages[i])) * 0.01
// 	}

// 	return messageCost
// }

// // don't edit below this line

// func test(messages []string) {
// 	costs := getMessageCosts(messages)
// 	fmt.Println("Messages:")
// 	for i := 0; i < len(messages); i++ {
// 		fmt.Printf(" - %v\n", messages[i])
// 	}
// 	fmt.Println("Costs:")
// 	for i := 0; i < len(costs); i++ {
// 		fmt.Printf(" - %.2f\n", costs[i])
// 	}
// 	fmt.Println("===== END REPORT =====")
// }

// func main() {
// 	test([]string{
// 		"Welcome to the movies!",
// 		"Enjoy your popcorn!",
// 		"Please don't talk during the movie!",
// 	})
// 	test([]string{
// 		"I don't want to be here anymore",
// 		"Can we go home?",
// 		"I'm hungry",
// 		"I'm bored",
// 	})
// 	test([]string{
// 		"Hello",
// 		"Hi",
// 		"Hey",
// 		"Hi there",
// 		"Hey there",
// 		"Hi there",
// 		"Hello there",
// 		"Hey there",
// 		"Hello there",
// 		"General Kenobi",
// 	})
// }

// package main

// import (
// 	"errors"
// 	"fmt"
// )

// const (
// 	planFree = "free"
// 	planPro  = "pro"
// )

// func getMessageWithRetriesForPlan(plan string) ([]string, error) {
// 	allMessages := getMessageWithRetries()
// 	if plan == "pro" {
// 		return allMessages[0:3], nil
// 	}

// 	if plan == "free" {
// 		return allMessages[0:2], nil
// 	}

// 	return []string{}, errors.New("unsupported plan")

// }

// // don't touch below this line

// func getMessageWithRetries() [3]string {
// 	return [3]string{
// 		"click here to sign up",
// 		"pretty please click here",
// 		"we beg you to sign up",
// 	}
// }

// func test(name string, doneAt int, plan string) {
// 	defer fmt.Println("=====================================")
// 	fmt.Printf("sending to %v...", name)
// 	fmt.Println()

// 	messages, err := getMessageWithRetriesForPlan(plan)
// 	if err != nil {
// 		fmt.Println("Error:", err)
// 		return
// 	}
// 	for i := 0; i < len(messages); i++ {
// 		msg := messages[i]
// 		fmt.Printf(`sending: "%v"`, msg)
// 		fmt.Println()
// 		if i == doneAt {
// 			fmt.Println("they responded!")
// 			break
// 		}
// 		if i == len(messages)-1 {
// 			fmt.Println("no response")
// 		}
// 	}
// }

// func main() {
// 	test("Ozgur", 3, planFree)
// 	test("Jeff", 3, planPro)
// 	test("Sally", 2, planPro)
// 	test("Sally", 3, "no plan")
// }

// // 01
// package main

// import "fmt"

// const (
// 	retry1 = "click here to sign up"
// 	retry2 = "pretty please click here"
// 	retry3 = "we beg you to sign up"
// )

// func getMessageWithRetries() [3]string {
// 	return [3]string{"click here to sign up", "pretty please click here", "we beg you to sign up"}
// }

// // don't touch below this line

// func testSend(name string, doneAt int) {
// 	fmt.Printf("sending to %v...", name)
// 	fmt.Println()

// 	messages := getMessageWithRetries()
// 	for i := 0; i < len(messages); i++ {
// 		msg := messages[i]
// 		fmt.Printf(`sending: "%v"`, msg)
// 		fmt.Println()
// 		if i == doneAt {
// 			fmt.Println("they responded!")
// 			break
// 		}
// 		if i == len(messages)-1 {
// 			fmt.Println("complete failure")
// 		}
// 	}
// }

// func main() {
// 	testSend("Bob", 0)
// 	testSend("Alice", 1)
// 	testSend("Mangalam", 2)
// 	testSend("Ozgur", 3)
// }
