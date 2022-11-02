// Connects to redis server and logs message to console
const redis = require('redis');
const redisCLI = redis.createClient();
const { promisify } = require('utils');

redisCLI
	.on('connect', () => {
		console.log('Redis client connected to the server');
	})
	.on('error', (err) => {
		console.log(`Redis client not connected to the server: ${err}`);
	});

const setNewSchool = (schoolName, value) => {
	redisCLI.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
	console.log(await promisify(redisCLI.get).bind(redisCLI)(schoolName));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
