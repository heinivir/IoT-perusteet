import express from 'express';

const app = express();
const PORT = 3000;

const DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1424387083765551186/tHCMhEjlC0_ExsYt_QV_d_qdbtNvKG3sANoJtpUclKgrMoywJmcniYPbnd27en6EATCF';

app.use(express.json());

app.post('/notify', (req, res) => {
  const { message } = req.body;

  if (!message) {
    return res.status(400).json({ error: 'Message is required' });
  }

  fetch(DISCORD_WEBHOOK_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ content: message })
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Discord responded with status ${response.status}`);
      }
      res.json({ status: 'Message sent...' });
    })
    .catch(error => {
      console.error('Error sending to Discord', error);
      res.status(500).json({ error: 'Failed sending your message' });
    });
});

app.listen(PORT, () => {
  console.log(`Server running at localhost:${PORT}`);
});
