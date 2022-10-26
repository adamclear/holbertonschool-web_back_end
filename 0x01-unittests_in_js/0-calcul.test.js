// Tests for 0-calcul.js
const calculateNumber = require('./0-calcul.js');
const assert = require('assert').strict;

describe('calculateNumber', () => {
	it('Testing positive ints and floats', () => {
		assert.equal(calculateNumber(2, 2), 4);
		assert.equal(calculateNumber(1.5, 1.5), 4);
		assert.equal(calculateNumber(1.5, 2), 4);
		assert.equal(calculateNumber(2, 1.5), 4);
	});
	it('Testing negative ints and floats', () => {
		assert.equal(calculateNumber(-2, -2), -4);
		assert.equal(calculateNumber(-2.5, -2.5), -4);
		assert.equal(calculateNumber(-2.5, -2), -4);
		assert.equal(calculateNumber(-2, -2.5), -4);
	});
	it('Testing TypeError', () => {
		assert.throws(() => calculateNumber(2, 'b'), TypeError);
		assert.throws(() => calculateNumber(NaN, 2), TypeError);
	});
});
