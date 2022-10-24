// Creates a small HTTP server using the http module
const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((request, response) => {
  if (request.url === '/') {
    response.end('Hello Holberton School!');
  } else if (request.url === '/students') {
    console.log('This is the list of our students');
    countStudents(process.argv[2]).then((data) => {
      response.end(data);
    })
    .catch((error) => response.end(data + error.message));
  }
})
  .listen(1245);

module.exports = app;
