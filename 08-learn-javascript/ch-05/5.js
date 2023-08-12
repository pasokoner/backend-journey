const movies = [
  "oh brother where art thou",
  "oceans eleven",
  "fight club",
  "the island",
  "shutter island",
  "the magnificent seven",
];

function logArray(arr) {
  for (const a of arr) {
    console.log(` - ${a}`);
  }
  console.log("---");
}

// don't touch above this line

logArray(movies.slice(2, movies.length));

logArray(movies.slice(0, movies.length - 2));
