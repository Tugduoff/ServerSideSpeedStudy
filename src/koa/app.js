const Koa = require('koa');
const Router = require('koa-router');

const app = new Koa();
const router = new Router();

router.get('/', async (ctx) => {
  ctx.body = { message: 'Hello World' };
});

router.get('/items/:item_id', async (ctx) => {
  const item_id = ctx.params.item_id;
  const q = ctx.query.q;
  ctx.body = { item_id: item_id, q: q };
});

router.get('/user/:user_id/workspace/:workspace_id/board/:board_id/list/:list_id/card/:card_id', async (ctx) => {
  const { user_id, workspace_id, board_id, list_id, card_id } = ctx.params;
  ctx.body = { user_id, workspace_id, board_id, list_id, card_id };
});

app
  .use(router.routes())
  .use(router.allowedMethods());

app.listen(8000, () => {
  console.log('Server is running on http://localhost:8000');
});
