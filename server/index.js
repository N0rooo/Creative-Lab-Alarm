const express = require('express');
const app = express();
const port = 3000

const ip = require('ip');

app.get('/send-msg', (req, res) => {
    res.json({ msg: 'Hello World!' })
});

app.get('/send', async (req, res) => {
    await fetch("https://discord.com/api/webhooks/1088081945122062458/vHX0UWK2pOXNnBeeAwT4C-qDESyjz576UmP0gHe5SP8DGlZEJo9WQX3-SWfTJQdDbOgH", {
        body: JSON.stringify({
            content: `@everyone INTRUSION DETECTED`,
        }),
        headers: {
            "Content-Type": "application/json",
        },
        method: "POST",
    });

    return res.json({ msg: 'Intrusion' })

});

app.listen(port, () => {
    console.log(ip.address());
})