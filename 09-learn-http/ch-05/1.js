try {
  printCharacterStats(4);
  printCharacterStats("ten");
  printCharacterStats(10);
} catch (error) {
  console.log(error);
}

// don't touch below this line

function printCharacterStats(level) {
  if (isNaN(level)) {
    throw new Error("Parameter is not a number!");
  }
  console.log(`Your character is level ${level}!`);
}
