function addID(movieRecord) {
  movieRecord.id = movieRecord.title + "" + movieRecord.username;

  return movieRecord;
}

// Don't touch below this line

function getMovieRecord(title, stars, username) {
  return {
    title: title,
    stars: stars,
    username: username,
  };
}

function logObject(obj) {
  for (const key in obj) {
    console.log(` - ${key}: ${obj[key]}`);
  }
  console.log("---");
}

const record = getMovieRecord("Frozen", 8.5, "Elsa");
logObject(record);
console.log("Adding ID...");
const idRecord = addID(record);
logObject(idRecord);
