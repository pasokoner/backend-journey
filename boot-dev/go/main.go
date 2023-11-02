package main

import "fmt"

func quicksort(nums *[]int, low int, high int) {
	if low >= high {
		return
	}

	p := partition(nums, low, high)

	quicksort(nums, low, p-1)
	quicksort(nums, p+1, high)
}

func partition(nums *[]int, low int, high int) int {
	pivot := (*nums)[high]
	i := low

	for j := low; j < high; j++ {
		if (*nums)[j] < pivot {
			(*nums)[i], (*nums)[j] = (*nums)[j], (*nums)[i]
			i++
		}
	}
	(*nums)[i], (*nums)[high] = (*nums)[high], (*nums)[i]

	return i
}

func main() {
	myNums := []int{5, 4, 3, 2, 1}

	quicksort(&myNums, 0, len(myNums)-1)

	fmt.Println(myNums)

}
