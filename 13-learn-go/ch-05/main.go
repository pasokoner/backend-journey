// 11
package main

import (
	"fmt"
)

func getExpenseReport(e expense) (string, float64) {
	switch v := e.(type) {
	case email:
		return v.toAddress, v.cost()
	case sms:
		return v.toPhoneNumber, v.cost()
	default:
		return "", 0.0
	}
}

// don't touch below this line

func (e email) cost() float64 {
	if !e.isSubscribed {
		return float64(len(e.body)) * .05
	}
	return float64(len(e.body)) * .01
}

func (s sms) cost() float64 {
	if !s.isSubscribed {
		return float64(len(s.body)) * .1
	}
	return float64(len(s.body)) * .03
}

func (i invalid) cost() float64 {
	return 0.0
}

type expense interface {
	cost() float64
}

type email struct {
	isSubscribed bool
	body         string
	toAddress    string
}

type sms struct {
	isSubscribed  bool
	body          string
	toPhoneNumber string
}

type invalid struct{}

func estimateYearlyCost(e expense, averageMessagesPerYear int) float64 {
	return e.cost() * float64(averageMessagesPerYear)
}

func test(e expense) {
	address, cost := getExpenseReport(e)
	switch e.(type) {
	case email:
		fmt.Printf("Report: The email going to %s will cost: %.2f\n", address, cost)
		fmt.Println("====================================")
	case sms:
		fmt.Printf("Report: The sms going to %s will cost: %.2f\n", address, cost)
		fmt.Println("====================================")
	default:
		fmt.Println("Report: Invalid expense")
		fmt.Println("====================================")
	}
}

func main() {
	test(email{
		isSubscribed: true,
		body:         "hello there",
		toAddress:    "john@does.com",
	})
	test(email{
		isSubscribed: false,
		body:         "This meeting could have been an email",
		toAddress:    "jane@doe.com",
	})
	test(email{
		isSubscribed: false,
		body:         "Wanna catch up later?",
		toAddress:    "elon@doe.com",
	})
	test(sms{
		isSubscribed:  false,
		body:          "I'm a Nigerian prince, please send me your bank info so I can deposit $1000 dollars",
		toPhoneNumber: "+155555509832",
	})
	test(sms{
		isSubscribed:  false,
		body:          "I don't need this",
		toPhoneNumber: "+155555504444",
	})
	test(invalid{})
}

// // 10
// package main

// import (
// 	"fmt"
// )

// func getExpenseReport(e expense) (string, float64) {
// 	newEmail, isEmail := e.(email)

// 	if isEmail {
// 		return newEmail.toAddress, newEmail.cost()
// 	}

// 	newSMS, isSMS := e.(sms)

// 	if isSMS {
// 		return newSMS.toPhoneNumber, newSMS.cost()
// 	}

// 	return "", 0.0
// }

// // don't touch below this line

// func (e email) cost() float64 {
// 	if !e.isSubscribed {
// 		return float64(len(e.body)) * .05
// 	}
// 	return float64(len(e.body)) * .01
// }

// func (s sms) cost() float64 {
// 	if !s.isSubscribed {
// 		return float64(len(s.body)) * .1
// 	}
// 	return float64(len(s.body)) * .03
// }

// func (i invalid) cost() float64 {
// 	return 0.0
// }

// type expense interface {
// 	cost() float64
// }

// type email struct {
// 	isSubscribed bool
// 	body         string
// 	toAddress    string
// }

// type sms struct {
// 	isSubscribed  bool
// 	body          string
// 	toPhoneNumber string
// }

// type invalid struct{}

// func estimateYearlyCost(e expense, averageMessagesPerYear int) float64 {
// 	return e.cost() * float64(averageMessagesPerYear)
// }

// func test(e expense) {
// 	address, cost := getExpenseReport(e)
// 	switch e.(type) {
// 	case email:
// 		fmt.Printf("Report: The email going to %s will cost: %.2f\n", address, cost)
// 		fmt.Println("====================================")
// 	case sms:
// 		fmt.Printf("Report: The sms going to %s will cost: %.2f\n", address, cost)
// 		fmt.Println("====================================")
// 	default:
// 		fmt.Println("Report: Invalid expense")
// 		fmt.Println("====================================")
// 	}
// }

// func main() {
// 	test(email{
// 		isSubscribed: true,
// 		body:         "hello there",
// 		toAddress:    "john@does.com",
// 	})
// 	test(email{
// 		isSubscribed: false,
// 		body:         "This meeting could have been an email",
// 		toAddress:    "jane@doe.com",
// 	})
// 	test(email{
// 		isSubscribed: false,
// 		body:         "This meeting could have been an email",
// 		toAddress:    "elon@doe.com",
// 	})
// 	test(sms{
// 		isSubscribed:  false,
// 		body:          "This meeting could have been an email",
// 		toPhoneNumber: "+155555509832",
// 	})
// 	test(sms{
// 		isSubscribed:  false,
// 		body:          "This meeting could have been an email",
// 		toPhoneNumber: "+155555504444",
// 	})
// 	test(invalid{})
// }

// 07
// package main

// import (
// 	"fmt"
// )

// func (e email) cost() float64 {
// 	if e.isSubscribed {
// 		return float64(len(e.body)) * 0.05
// 	}

// 	return float64(len(e.body)) * .01
// }

// func (e email) print() {
// 	fmt.Printf("%s", e.body)
// }

// // don't touch below this line

// type expense interface {
// 	cost() float64
// }

// type printer interface {
// 	print()
// }

// type email struct {
// 	isSubscribed bool
// 	body         string
// }

// func print(p printer) {
// 	p.print()
// }

// func test(e expense, p printer) {
// 	fmt.Printf("Printing with cost: $%.2f ...\n", e.cost())
// 	p.print()
// 	fmt.Println("====================================")
// }

// func main() {
// 	e := email{
// 		isSubscribed: true,
// 		body:         "hello there",
// 	}
// 	test(e, e)
// 	e = email{
// 		isSubscribed: false,
// 		body:         "I want my money back",
// 	}
// 	test(e, e)
// 	e = email{
// 		isSubscribed: true,
// 		body:         "Are you free for a chat?",
// 	}
// 	test(e, e)
// 	e = email{
// 		isSubscribed: false,
// 		body:         "This meeting could have been an email",
// 	}
// 	test(e, e)
// }

// // 02
// package main

// import (
// 	"fmt"
// )

// type employee interface {
// 	getName() string
// 	getSalary() int
// }

// type contractor struct {
// 	name         string
// 	hourlyPay    int
// 	hoursPerYear int
// }

// func (c contractor) getName() string {
// 	return c.name
// }

// func (c contractor) getSalary() int {
// 	return c.hourlyPay * c.hoursPerYear
// }

// // don't touch below this line

// type fullTime struct {
// 	name   string
// 	salary int
// }

// func (ft fullTime) getSalary() int {
// 	return ft.salary
// }

// func (ft fullTime) getName() string {
// 	return ft.name
// }

// func test(e employee) {
// 	fmt.Println(e.getName(), e.getSalary())
// 	fmt.Println("====================================")
// }

// func main() {
// 	test(fullTime{
// 		name:   "Jack",
// 		salary: 50000,
// 	})
// 	test(contractor{
// 		name:         "Bob",
// 		hourlyPay:    100,
// 		hoursPerYear: 73,
// 	})
// 	test(contractor{
// 		name:         "Jill",
// 		hourlyPay:    872,
// 		hoursPerYear: 982,
// 	})
// }

// // 01
// package main

// import (
// 	"fmt"
// 	"time"
// )

// func sendMessage(msg message) {
// 	fmt.Println(msg.getMessage())
// }

// type message interface {
// 	getMessage() string
// }

// // don't edit below this line

// type birthdayMessage struct {
// 	birthdayTime  time.Time
// 	recipientName string
// }

// func (bm birthdayMessage) getMessage() string {
// 	return fmt.Sprintf("Hi %s, it is your birthday on %s", bm.recipientName, bm.birthdayTime.Format(time.RFC3339))
// }

// type sendingReport struct {
// 	reportName    string
// 	numberOfSends int
// }

// func (sr sendingReport) getMessage() string {
// 	return fmt.Sprintf(`Your "%s" report is ready. You've sent %v messages.`, sr.reportName, sr.numberOfSends)
// }

// func test(m message) {
// 	sendMessage(m)
// 	fmt.Println("====================================")
// }

// func main() {
// 	test(sendingReport{
// 		reportName:    "First Report",
// 		numberOfSends: 10,
// 	})
// 	test(birthdayMessage{
// 		recipientName: "John Doe",
// 		birthdayTime:  time.Date(1994, 03, 21, 0, 0, 0, 0, time.UTC),
// 	})
// 	test(sendingReport{
// 		reportName:    "First Report",
// 		numberOfSends: 10,
// 	})
// 	test(birthdayMessage{
// 		recipientName: "Bill Deer",
// 		birthdayTime:  time.Date(1934, 05, 01, 0, 0, 0, 0, time.UTC),
// 	})
// }
