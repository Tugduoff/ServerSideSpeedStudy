const express = require('express');
const app = express();
const port = 8000;

app.get('/', (req, res) => {
  res.json({ message: 'Hello World' });
});

app.get('/items/:item_id', (req, res) => {
  const item_id = req.params.item_id;
  const q = req.query.q;
  res.json({ item_id: item_id, q: q });
});

app.get('/user/:user_id/workspace/:workspace_id/board/:board_id/list/:list_id/card/:card_id', (req, res) => {
  const { user_id, workspace_id, board_id, list_id, card_id } = req.params;
  res.json({ user_id, workspace_id, board_id, list_id, card_id });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
