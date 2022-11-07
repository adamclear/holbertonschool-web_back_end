// Small stock server for task 12
// Array of products
const listProducts = [
	{
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
    currentQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
    currentQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
    currentQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
    currentQuantity: 5,
  },
];

// Functions
function getItemById(id) {
	return listProducts.find(item => item.itemId === id);
};
async function reserveStockById(itemId, stock) {
	await asyncSet(`item.${itemId}`, stock);
};
async function getCurrentReservedStockById(itemId) {
	await asyncGet(`item.${itemId}`);
};

// Express server with routes
const express = require('express');
const app = express();
app.listen(1245);

app.get('/list_products', (request, response) => {
	response.send(listProducts);
});
app.get('/list_products/:itemId', (request, response) => {
	const itemId = request.params.itemId;
	const item = getItemById(Number(itemId));
	if (item) {
		getCurrentReservedStockById(itemId).then(() => {
			response.send(item);
		});
	} else {
		response.status(404).send(
			{
				status: 'Product not found'
			}
		);
	}
});
app.get('/reserve_product/:itemId', (request, response) => {
	const itemId = request.params.itemId;
	const item = getItemById(Number(itemId));
	if (item) {
		if (item.currentQuantity <= 0) {
			response.status(400).send(
				{
					status: 'Not enough stock available',
					itemId: itemId
				}
			);
		} else {
			item.currentQuantity--;
			reserveStockById(itemId, item.currentQuantity);
			response.send(
				{
					status: 'Reservation confirmed',
					itemId: itemId
				}
			);
		}
	} else {
		return response.status(404).send(
			{
				status: 'Product not found'
			}
		);
	}
});

// Redis client
const redis = require('redis');
const redisCLI = redis.createClient();
const { promisify } = require('util');
const asyncGet = promisify(redisCLI.get).bind(redisCLI);
const asyncSet = promisify(redisCLI.set).bind(redisCLI);
