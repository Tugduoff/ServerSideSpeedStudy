require 'sinatra'
require 'json'

# Define the root route
get '/' do
  content_type :json
  { message: "Hello World" }.to_json
end

# Define the item route
get '/items/:item_id' do
  content_type :json
  item_id = params['item_id']
  q = params['q']
  { item_id: item_id, q: q }.to_json
end

# Define the card route
get '/user/:user_id/workspace/:workspace_id/board/:board_id/list/:list_id/card/:card_id' do
  content_type :json
  {
    user_id: params['user_id'],
    workspace_id: params['workspace_id'],
    board_id: params['board_id'],
    list_id: params['list_id'],
    card_id: params['card_id']
  }.to_json
end
