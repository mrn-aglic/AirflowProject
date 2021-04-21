const index = require('./index');
const run = index.run;

const express = require('express');
const app = express()
const port = 3000;
const host = '0.0.0.0';

app.get('/', async (req, res) => {
    const result = await run();
    res.send(`Hello world from node: ${result}`);
});

app.listen(port, host, () => {
    console.log(`Listening on: ${host}:${port}`);
});
