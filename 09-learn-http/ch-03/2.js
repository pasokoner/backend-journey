function printURLParts(urlString) {
  const urlObj = new URL(urlString);
  for (const key in urlObj) {
    console.log(urlObj[key]);
  }
}

// don't touch below this line

const fantasyQuestURL = "http://dragonslayer:pwn3d@fantasyquest.com:8080/maps?sort=rank#id";
printURLParts(fantasyQuestURL);
