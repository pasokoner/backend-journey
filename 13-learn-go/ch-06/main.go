// 06
package main

import (
	"errors"
	"fmt"
)

func divide(x, y float64) (float64, error) {
	if y == 0 {
		return 0.0, errors.New("no dividing by 0")
	}
	return x / y, nil
}

// don't edit below this line

func test(x, y float64) {
	defer fmt.Println("====================================")
	fmt.Printf("Dividing %.2f by %.2f ...\n", x, y)
	quotient, err := divide(x, y)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("Quotient: %.2f\n", quotient)
}

func main() {
	test(10, 0)
	test(10, 2)
	test(15, 30)
	test(6, 3)
}

// // 03
// package main

// import (
// 	"fmt"
// )

// type divideError struct {
// 	dividend float64
// }

// func (d divideError) Error() string {
// 	return fmt.Sprintf("can not divide %v by zero", d.dividend)
// }

// // don't edit below this line

// func divide(dividend, divisor float64) (float64, error) {
// 	if divisor == 0 {
// 		// We convert the `divideError` struct to an `error` type by returning it
// 		// as an error. As an error type, when it's printed its default value
// 		// will be the result of the Error() method
// 		return 0, divideError{dividend: dividend}
// 	}
// 	return dividend / divisor, nil
// }

// func test(dividend, divisor float64) {
// 	defer fmt.Println("====================================")
// 	fmt.Printf("Dividing %.2f by %.2f ...\n", dividend, divisor)
// 	quotient, err := divide(dividend, divisor)
// 	if err != nil {
// 		fmt.Println(err)
// 		return
// 	}
// 	fmt.Printf("Quotient: %.2f\n", quotient)
// }

// func main() {
// 	test(10, 0)
// 	test(10, 2)
// 	test(15, 30)
// 	test(6, 3)
// }

// // 02
// package main

// import (
// 	"fmt"
// )

// func getSMSErrorString(cost float64, recipient string) string {
// 	return fmt.Sprintf("SMS that costs $%.2f to be sent to '%v' can not be sent", cost, recipient)
// }

// // don't edit below this line

// func test(cost float64, recipient string) {
// 	s := getSMSErrorString(cost, recipient)
// 	fmt.Println(s)
// 	fmt.Println("====================================")
// }

// func main() {
// 	test(1.4, "+1 (435) 555 0923")
// 	test(2.1, "+2 (702) 555 3452")
// 	test(32.1, "+1 (801) 555 7456")
// 	test(14.4, "+1 (234) 555 6545")
// }

// // 01
// package main

// import (
// 	"fmt"
// )

// func sendSMSToCouple(msgToCustomer, msgToSpouse string) (float64, error) {
// 	customer, err := sendSMS(msgToCustomer)

// 	if err != nil {
// 		return 0.0, err
// 	}

// 	spouse, err := sendSMS(msgToSpouse)

// 	if err != nil {
// 		return 0.0, err
// 	}

// 	return customer + spouse, nil
// }

// // don't edit below this line

// func sendSMS(message string) (float64, error) {
// 	const maxTextLen = 25
// 	const costPerChar = .0002
// 	if len(message) > maxTextLen {
// 		return 0.0, fmt.Errorf("can't send texts over %v characters", maxTextLen)
// 	}
// 	return costPerChar * float64(len(message)), nil
// }

// func test(msgToCustomer, msgToSpouse string) {
// 	defer fmt.Println("========")
// 	fmt.Println("Message for customer:", msgToCustomer)
// 	fmt.Println("Message for spouse:", msgToSpouse)
// 	totalCost, err := sendSMSToCouple(msgToCustomer, msgToSpouse)
// 	if err != nil {
// 		fmt.Println("Error:", err)
// 		return
// 	}
// 	fmt.Printf("Total cost: $%.4f\n", totalCost)
// }

// func main() {
// 	test(
// 		"Thanks for coming in to our flower shop today!",
// 		"We hope you enjoyed your gift.",
// 	)
// 	test(
// 		"Thanks for joining us!",
// 		"Have a good day.",
// 	)
// 	test(
// 		"Thank you.",
// 		"Enjoy!",
// 	)
// 	test(
// 		"We loved having you in!",
// 		"We hope the rest of your evening is absolutely fantastic.",
// 	)
// }
