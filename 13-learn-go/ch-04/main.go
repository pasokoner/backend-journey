// 06
package main

import "fmt"

type authenticationInfo struct {
	username string
	password string
}

func (auth authenticationInfo) getBasicAuth() string {
	return fmt.Sprintf("Authorization: Basic %s:%s", auth.username, auth.password)
}

// don't touch below this line

func test(authInfo authenticationInfo) {
	fmt.Println(authInfo.getBasicAuth())
	fmt.Println("====================================")
}

func main() {
	test(authenticationInfo{
		username: "Google",
		password: "12345",
	})
	test(authenticationInfo{
		username: "Bing",
		password: "98765",
	})
	test(authenticationInfo{
		username: "DDG",
		password: "76921",
	})
}

// // 05
// package main

// import "fmt"

// type sender struct {
// 	rateLimit int
// 	user
// }

// type user struct {
// 	name   string
// 	number int
// }

// // don't edit below this line

// func test(s sender) {
// 	fmt.Println("Sender name:", s.name)
// 	fmt.Println("Sender number:", s.number)
// 	fmt.Println("Sender rateLimit:", s.rateLimit)
// 	fmt.Println("====================================")
// }

// func main() {
// 	test(sender{
// 		rateLimit: 10000,
// 		user: user{
// 			name:   "Deborah",
// 			number: 18055558790,
// 		},
// 	})
// 	test(sender{
// 		rateLimit: 5000,
// 		user: user{
// 			name:   "Sarah",
// 			number: 19055558790,
// 		},
// 	})
// 	test(sender{
// 		rateLimit: 1000,
// 		user: user{
// 			name:   "Sally",
// 			number: 19055558790,
// 		},
// 	})
// }

// // 02
// package main

// import (
// 	"fmt"
// )

// type messageToSend struct {
// 	message   string
// 	sender    user
// 	recipient user
// }

// type user struct {
// 	name   string
// 	number int
// }

// func canSendMessage(mToSend messageToSend) bool {

// 	if mToSend.sender.name == "" && mToSend.sender.number == 0 && mToSend.recipient.name == "" && mToSend.recipient.number == 0 {
// 		return true
// 	}

// 	return false
// }

// // don't touch below this line

// func test(mToSend messageToSend) {
// 	fmt.Printf(`sending "%s" from %s (%v) to %s (%v)...`,
// 		mToSend.message,
// 		mToSend.sender.name,
// 		mToSend.sender.number,
// 		mToSend.recipient.name,
// 		mToSend.recipient.number,
// 	)
// 	fmt.Println()
// 	if canSendMessage(mToSend) {
// 		fmt.Println("...sent!")
// 	} else {
// 		fmt.Println("...can't send message")
// 	}
// 	fmt.Println("====================================")
// }

// func main() {
// 	test(messageToSend{
// 		message: "you have an appointment tommorow",
// 		sender: user{
// 			name:   "Brenda Halafax",
// 			number: 16545550987,
// 		},
// 		recipient: user{
// 			name:   "Sally Sue",
// 			number: 19035558973,
// 		},
// 	})
// 	test(messageToSend{
// 		message: "you have an event tommorow",
// 		sender: user{
// 			number: 16545550987,
// 		},
// 		recipient: user{
// 			name:   "Suzie Sall",
// 			number: 0,
// 		},
// 	})
// 	test(messageToSend{
// 		message: "you have an party tommorow",
// 		sender: user{
// 			name:   "Njorn Halafax",
// 			number: 16545550987,
// 		},
// 		recipient: user{
// 			name:   "Sally Sue",
// 			number: 19035558973,
// 		},
// 	})
// 	test(messageToSend{
// 		message: "you have a birthday tommorow",
// 		sender: user{
// 			name:   "Eli Halafax",
// 			number: 0,
// 		},
// 		recipient: user{
// 			name:   "Whitaker Sue",
// 			number: 19035558973,
// 		},
// 	})
// }

// // 01
// package main

// import "fmt"

// type messageToSend struct {
// 	phoneNumber int
// 	message     string
// }

// // don't edit below this line

// func test(m messageToSend) {
// 	fmt.Printf("Sending message: '%s' to: %v\n", m.message, m.phoneNumber)
// 	fmt.Println("====================================")
// }

// func main() {
// 	test(messageToSend{
// 		phoneNumber: 148255510981,
// 		message:     "Thanks for signing up",
// 	})
// 	test(messageToSend{
// 		phoneNumber: 148255510982,
// 		message:     "Love to have you aboard!",
// 	})
// 	test(messageToSend{
// 		phoneNumber: 148255510983,
// 		message:     "We're so excited to have you",
// 	})
// }
