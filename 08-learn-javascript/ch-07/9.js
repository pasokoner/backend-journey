const user = {
  getLatestReview() {
    // ?
  },
  reviews: ["I hate Ice Age", "I didn't enjoy it at all", "What a fabulous film"],
  name: "Bob Doogle",
  getLatestReview() {
    return this.reviews[0];
  },
};

// don't touch below this line

console.log(`${user.name}'s latest review is: ${user.getLatestReview()}`);
