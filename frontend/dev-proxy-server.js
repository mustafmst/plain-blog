const Bundler = require('parcel-bundler');
const express = require('express');
const proxy = require('http-proxy-middleware');

const port = 3000
console.log(`Port numeber of app proxy: ${port}`)

const app = express();

app.use('/api', proxy({
  target: 'http://localhost:8000'
}));

const bundler = new Bundler('src/index.html');
app.use(bundler.middleware());

app.listen(port);
