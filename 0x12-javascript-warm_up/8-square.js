#!/usr/bin/node

const args = process.argv.slice(2);
const size = parseInt(args[0], 10);
if(args.length === 0 || !Number.isInteger(size) || Number.isNaN(size)){
	console.log('Missing size');
} else{
	for(let i = 0; i < size ; i++){
		let row = "";
		for(let j = 0; j < size; j++){
			row += "X";
		}
		console.log(row);
	}
}

