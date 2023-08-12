const movieExists = (movies, movie) => {
  for (m of movies) {
    if (movie === m) {
      console.log(`Found: ${movie}`);
    }
  }
};

// don't touch below this line

movieExists(["Incredibles", "Tangled", "Frozen"], "Frozen");
console.log("---");
movieExists(["The Quick and the Dead", "The Magnificent 7", "Frozen"], "The Magnificent 7");
console.log("---");
movieExists(["Dead", "Alive", "Flight", "Rocky"], "Flight");
console.log("---");
movieExists(["Dead", "Alive", "Flight", "Rocky"], "None");
console.log("---");
