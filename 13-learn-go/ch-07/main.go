package main

import (
	"fmt"
	"math"
)

func printPrimes(max int) {
	for i := 2; i < max + 1; i++ {
		if i == 2 {
			fmt.Println(i)
		}

		if i % 2 == 0 {
			continue
		}

		for j := 3; j < int(math.Sqrt(float64(i))) + 1; i++ {
			if j %
		}

	}

}

// don't edit below this line

func test(max int) {
	fmt.Printf("Primes up to %v:\n", max)
	printPrimes(max)
	fmt.Println("===============================================================")
}

func main() {
	test(10)
	test(20)
	test(30)
}

// // 05
// package main

// import "fmt"

// func fizzbuzz() {

// 	for i := 1; i <= 100; i++ {
// 		buzzin := ""
// 		if i%3 == 0 {
// 			buzzin += "fizz"
// 		}

// 		if i%5 == 0 {
// 			buzzin += "buzz"
// 		}

// 		if buzzin == "" {
// 			fmt.Println(i)
// 		} else {
// 			fmt.Println(buzzin)
// 		}
// 	}

// }

// // don't touch below this line

// func main() {
// 	fizzbuzz()
// }

// // 03
// package main

// import (
// 	"fmt"
// )

// func getMaxMessagesToSend(costMultiplier float64, maxCostInPennies int) int {
// 	actualCostInPennies := 1.0
// 	maxMessagesToSend := 0
// 	for actualCostInPennies <= float64(maxCostInPennies) {
// 		actualCostInPennies *= costMultiplier
// 		maxMessagesToSend++
// 	}
// 	if int(actualCostInPennies) > maxCostInPennies {
// 		maxMessagesToSend--
// 	}
// 	return maxMessagesToSend
// }

// // don't touch below this line

// func test(costMultiplier float64, maxCostInPennies int) {
// 	maxMessagesToSend := getMaxMessagesToSend(costMultiplier, maxCostInPennies)
// 	fmt.Printf("Multiplier: %v\n",
// 		costMultiplier,
// 	)
// 	fmt.Printf("Max cost: %v\n",
// 		maxCostInPennies,
// 	)
// 	fmt.Printf("Max messages you can send: %v\n",
// 		maxMessagesToSend,
// 	)
// 	fmt.Println("====================================")
// }

// func main() {
// 	test(1.1, 5)
// 	test(1.3, 10)
// 	test(1.35, 25)
// }

// // 01
// package main

// import (
// 	"fmt"
// )

// func bulkSend(numMessages int) float64 {
// 	var total float64
// 	for i := 0; i < numMessages; i++ {
// 		total += 1.0 + (0.01 * float64(i))
// 	}

// 	return total
// }

// // don't edit below this line

// func test(numMessages int) {
// 	fmt.Printf("Sending %v messages\n", numMessages)
// 	cost := bulkSend(numMessages)
// 	fmt.Printf("Bulk send complete! Cost = %.2f\n", cost)
// 	fmt.Println("===============================================================")
// }

// func main() {
// 	test(10)
// 	test(20)
// 	test(30)
// 	test(40)
// 	test(50)
// }
