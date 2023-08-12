function getMovieRecord(title, stars, username) {
  return {
    id: title + "-" + username,
    title,
    stars,
    username,
  };
}

// Don't touch below this line

logObject(getMovieRecord("oh brother where art thou", 3, "wagslane"));
logObject(getMovieRecord("frozen", 5.5, "elonmusk"));
logObject(getMovieRecord("toy story", 4, "prince"));

function logObject(obj) {
  for (const key in obj) {
    console.log(` - ${key}: ${obj[key]}`);
  }
  console.log("---");
}
