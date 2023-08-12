function getCleanRank(reviewWords) {
  const profanity = ["dang", "shoot", "heck"];
  let counter = 0;

  if (reviewWords.includes(profanity[0])) {
    counter += 1;
  }

  if (reviewWords.includes(profanity[1])) {
    counter += 1;
  }

  if (reviewWords.includes(profanity[2])) {
    counter += 1;
  }

  if (counter === 1) {
    return "dirty";
  }

  if (counter >= 2) {
    return "filthy";
  }

  return "clean";
}

// Don't edit below this line

function test(reviewWords) {
  const cleanRank = getCleanRank(reviewWords);
  console.log(`'${reviewWords}' has rank: ${cleanRank}`);
}

test(["avril", "lavigne", "has", "best", "dang", "tour"]);
test(["what", "a", "bad", "film"]);
test(["oh", "my", "heck", "I", "hated", "it"]);
test(["ripoff"]);
test(["That", "was", "a", "pleasure"]);
test(["shoot!", "I", "cant", "say", "I", "liked", "the", "dang", "thing"]);
test(["shoot", "dang", "heck"]);
